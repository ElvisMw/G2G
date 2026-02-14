from django.contrib import admin
from .models import Payment, Remittance, RevenueLog

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
	list_display = ("id", "vehicle_id", "contract_id", "paid_from", "paid_to", "amount", "payment_type", "mpesa_code", "phone_number", "date_paid", "recorded_at")
	search_fields = ("mpesa_code", "paid_from", "paid_to", "phone_number")
	list_filter = ("payment_type", "date_paid", "recorded_at")

@admin.register(Remittance)
class RemittanceAdmin(admin.ModelAdmin):
	list_display = ("id", "contract_id", "rider_id", "amount", "date", "created_at")
	search_fields = ("contract_id", "rider_id")
	list_filter = ("date",)

@admin.register(RevenueLog)
class RevenueLogAdmin(admin.ModelAdmin):
	list_display = ("id", "vehicle_id", "date", "expected_revenue", "actual_revenue", "created_at")
	search_fields = ("vehicle_id",)
	list_filter = ("date",)
