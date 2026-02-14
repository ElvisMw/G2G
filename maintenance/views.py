from django.shortcuts import render


from .models import MaintenanceRecord, OdometerLog, ServiceRecord, ComponentRecord, DowntimeLog

def maintenance_list(request):
	maintenance_records = MaintenanceRecord.objects.all()
	return render(request, "maintenance.html", {"maintenance_records": maintenance_records})

def odometer_log_list(request):
	odometer_logs = OdometerLog.objects.all()
	return render(request, "odometer_logs.html", {"odometer_logs": odometer_logs})

def service_record_list(request):
	service_records = ServiceRecord.objects.all()
	return render(request, "service_records.html", {"service_records": service_records})

def component_record_list(request):
	component_records = ComponentRecord.objects.all()
	return render(request, "component_records.html", {"component_records": component_records})

def downtime_log_list(request):
	downtime_logs = DowntimeLog.objects.all()
	return render(request, "downtime_logs.html", {"downtime_logs": downtime_logs})
