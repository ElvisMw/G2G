from django.contrib import admin


from .models import Report, DashboardMetric
import csv
import tablib
from django.http import HttpResponse
from django.utils.html import format_html
from django.contrib import messages
try:
	import pandas as pd
except ImportError:
	pd = None
try:
	from reportlab.pdfgen import canvas
	from reportlab.lib.pagesizes import letter
	from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Image, Paragraph, Spacer
	from reportlab.lib import colors
	from reportlab.lib.styles import getSampleStyleSheet
	import os
except ImportError:
	canvas = None


def export_as_excel(modeladmin, request, queryset):
	if pd is None:
		messages.error(request, "Pandas is required for Excel export. Please install it.")
		return
	data = []
	field_names = [field.name for field in modeladmin.model._meta.fields]
	for obj in queryset:
		data.append([getattr(obj, field) for field in field_names])
	df = pd.DataFrame(data, columns=field_names)
	response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
	response['Content-Disposition'] = 'attachment; filename={}.xlsx'.format(modeladmin.model.__name__)
	df.to_excel(response, index=False)
	return response

def export_as_pdf(modeladmin, request, queryset):
	if canvas is None:
		messages.error(request, "ReportLab is required for PDF export. Please install it.")
		return
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename={}.pdf'.format(modeladmin.model.__name__)

	# Prepare data
	field_names = [field.verbose_name.title() for field in modeladmin.model._meta.fields]
	data = [field_names]
	for obj in queryset:
		data.append([str(getattr(obj, field.name)) for field in modeladmin.model._meta.fields])

	# Build PDF
	doc = SimpleDocTemplate(response, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=60, bottomMargin=30)
	elements = []
	styles = getSampleStyleSheet()

	# Add logo if available
	logo_path = os.path.join('static', 'images', 'logo.png')
	if os.path.exists(logo_path):
		elements.append(Image(logo_path, width=80, height=80))
		elements.append(Spacer(1, 12))

	# Add title
	title = f"{modeladmin.model._meta.verbose_name_plural.title()} Export"
	elements.append(Paragraph(title, styles['Title']))
	elements.append(Spacer(1, 12))

	# Add table
	table = Table(data, repeatRows=1)
	table.setStyle(TableStyle([
		('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2563eb')),
		('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
		('ALIGN', (0, 0), (-1, -1), 'CENTER'),
		('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
		('FONTSIZE', (0, 0), (-1, 0), 11),
		('BOTTOMPADDING', (0, 0), (-1, 0), 10),
		('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
		('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
		('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#2563eb')),
	]))
	elements.append(table)

	doc.build(elements)
	return response

export_as_excel.short_description = "Export selected as Excel"
export_as_pdf.short_description = "Export selected as PDF"

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
	list_display = ("report_type", "generated_for", "generated_at")
	search_fields = ("report_type", "generated_for")
	list_filter = ("report_type", "generated_at")
	actions = [export_as_excel, export_as_pdf]


@admin.register(DashboardMetric)
class DashboardMetricAdmin(admin.ModelAdmin):
	list_display = ("metric_type", "value", "calculated_at")
	search_fields = ("metric_type", "value")
	list_filter = ("metric_type", "calculated_at")
	actions = [export_as_excel, export_as_pdf]
