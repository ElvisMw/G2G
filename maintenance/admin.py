from django.contrib import admin

from .models import MaintenanceRecord, OdometerLog, ServiceRecord, ComponentRecord, DowntimeLog

@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):
	list_display = ("vehicle_id", "date", "category", "amount", "created_at")
	search_fields = ("vehicle_id", "description")
	list_filter = ("category", "date")

@admin.register(OdometerLog)
class OdometerLogAdmin(admin.ModelAdmin):
	list_display = ("vehicle_id", "date", "mileage", "created_at")
	search_fields = ("vehicle_id",)
	list_filter = ("date",)

@admin.register(ServiceRecord)
class ServiceRecordAdmin(admin.ModelAdmin):
	list_display = ("vehicle_id", "service_type", "mechanic", "service_date", "cost")
	search_fields = ("vehicle_id", "service_type", "mechanic")
	list_filter = ("service_type", "service_date")

@admin.register(ComponentRecord)
class ComponentRecordAdmin(admin.ModelAdmin):
	list_display = ("vehicle_id", "component_name", "supplier", "purchase_date", "cost")
	search_fields = ("vehicle_id", "component_name", "supplier")
	list_filter = ("component_name", "supplier")

@admin.register(DowntimeLog)
class DowntimeLogAdmin(admin.ModelAdmin):
	list_display = ("vehicle_id", "reason", "start_date", "end_date")
	search_fields = ("vehicle_id", "reason")
	list_filter = ("reason", "start_date")
