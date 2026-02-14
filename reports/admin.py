from django.contrib import admin

from .models import Report, DashboardMetric

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
	list_display = ("report_type", "generated_for", "generated_at")
	search_fields = ("report_type", "generated_for")
	list_filter = ("report_type", "generated_at")

@admin.register(DashboardMetric)
class DashboardMetricAdmin(admin.ModelAdmin):
	list_display = ("metric_type", "value", "calculated_at")
	search_fields = ("metric_type", "value")
	list_filter = ("metric_type", "calculated_at")
