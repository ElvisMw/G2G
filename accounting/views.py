from django.shortcuts import render


from .models import Account, JournalEntry, AuditLog

def account_list(request):
	accounts = Account.objects.all()
	return render(request, "accounting.html", {"accounts": accounts})

def journal_entry_list(request):
	entries = JournalEntry.objects.all()
	return render(request, "journal_entries.html", {"entries": entries})

def audit_log_list(request):
	logs = AuditLog.objects.all()
	return render(request, "audit_logs.html", {"logs": logs})
