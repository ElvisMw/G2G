from django.contrib import admin

from .models import Rider

@admin.register(Rider)
class RiderAdmin(admin.ModelAdmin):
	list_display = ("first_name", "last_name", "national_id", "phone_number", "status", "created_at")
	search_fields = ("first_name", "last_name", "national_id", "phone_number")
	list_filter = ("status",)
