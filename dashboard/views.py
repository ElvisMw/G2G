from fleet.models import Vehicle
from riders.models import Rider
from finance.models import Payment
from django.db.models import Sum

def dashboard(request):
	total_vehicles = Vehicle.objects.count()
	total_riders = Rider.objects.count()
	total_outstanding = Vehicle.objects.aggregate(total=Sum('outstanding_balance'))['total'] or 0
	total_revenue = Payment.objects.filter(payment_type='INSTALLMENT').aggregate(total=Sum('amount'))['total'] or 0

	from finance.models import Payment as PaymentModel
	from maintenance.models import MaintenanceRecord
	from contracts.models import Contract
	from django.utils import timezone

	recent_payments = PaymentModel.objects.order_by('-date_paid')[:5]
	recent_maintenance = MaintenanceRecord.objects.order_by('-date')[:5]
	recent_contracts = Contract.objects.order_by('-start_date')[:5]

	return render(request, 'dashboard.html', {
		'total_vehicles': total_vehicles,
		'total_riders': total_riders,
		'total_outstanding': total_outstanding,
		'total_revenue': total_revenue,
		'recent_payments': recent_payments,
		'recent_maintenance': recent_maintenance,
		'recent_contracts': recent_contracts,
		'now': timezone.now(),
	})
from django.shortcuts import render

# Create your views here.
