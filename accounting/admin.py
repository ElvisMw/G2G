from django.contrib import admin

from .models import Account, JournalEntry, AuditLog

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
	list_display = ("name", "account_type", "description")
	search_fields = ("name",)
	list_filter = ("account_type",)

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
	list_display = ("date", "account", "debit", "credit", "balance", "is_deleted", "immutable", "created_at")
	search_fields = ("description",)
	list_filter = ("date", "is_deleted", "immutable")

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
	list_display = ("action", "model_name", "user_id", "object_id", "timestamp")
	search_fields = ("model_name", "user_id", "object_id")
	list_filter = ("action", "model_name")
