from django.urls import path
from .views import account_list, journal_entry_list, audit_log_list

urlpatterns = [
    path('', account_list, name='account_list'),
    path('journal-entries/', journal_entry_list, name='journal_entry_list'),
    path('audit-logs/', audit_log_list, name='audit_log_list'),
]
