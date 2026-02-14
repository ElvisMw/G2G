from django.contrib import admin

from .models import ComplianceDocument

@admin.register(ComplianceDocument)
class ComplianceDocumentAdmin(admin.ModelAdmin):
	list_display = ("name", "number", "vehicle_id", "issue_date", "expiry_date", "status", "created_at")
	search_fields = ("name", "number", "vehicle_id")
	list_filter = ("status", "issue_date", "expiry_date")
