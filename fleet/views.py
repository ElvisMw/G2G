from django.shortcuts import render


from .models import Vehicle

def vehicle_list(request):
	vehicles = Vehicle.objects.all()
	return render(request, "vehicles.html", {"vehicles": vehicles})

def vehicle_detail(request, pk):
	vehicle = Vehicle.objects.get(pk=pk)
	# Calculate deductions: sum of maintenance and relevant payments
	from maintenance.models import MaintenanceRecord
	from finance.models import Payment
	from django.db.models import Sum

	# Maintenance deductions
	maintenance_deductions = MaintenanceRecord.objects.filter(vehicle_id=vehicle.id).values('category').annotate(total=Sum('amount'))
	# Payment deductions (penalty, insurance, service, repair, other)
	payment_types = ["PENALTY", "INSURANCE", "SERVICE", "REPAIR", "OTHER"]
	payment_deductions = Payment.objects.filter(vehicle_id=vehicle.id, payment_type__in=payment_types).values('payment_type').annotate(total=Sum('amount'))

	# Breakdown as list of dicts
	deduction_breakdown = []
	for m in maintenance_deductions:
		deduction_breakdown.append({
			'type': m['category'].title().replace('_', ' '),
			'amount': m['total'] or 0
		})
	for p in payment_deductions:
		deduction_breakdown.append({
			'type': p['payment_type'].title(),
			'amount': p['total'] or 0
		})

	total_deductions = sum(item['amount'] for item in deduction_breakdown)

	return render(request, "vehicle_detail.html", {
		"vehicle": vehicle,
		"deduction_breakdown": deduction_breakdown,
		"total_deductions": total_deductions
	})
