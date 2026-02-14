from django.contrib import admin

from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
	list_display = ("id", "vehicle_id", "rider_id", "start_date", "end_date", "revenue_model", "status", "created_at")
	search_fields = ("id", "vehicle_id", "rider_id")
	list_filter = ("status", "revenue_model")
