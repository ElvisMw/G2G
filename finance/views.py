from django.shortcuts import render


from .models import Payment, Remittance, RevenueLog

def payment_list(request):
	payments = Payment.objects.all()
	return render(request, "payments.html", {"payments": payments})

def remittance_list(request):
	remittances = Remittance.objects.all()
	return render(request, "remittances.html", {"remittances": remittances})

def revenue_log_list(request):
	revenue_logs = RevenueLog.objects.all()
	return render(request, "revenue_logs.html", {"revenue_logs": revenue_logs})
