from django.shortcuts import render


from .models import Report, DashboardMetric

def report_list(request):
	reports = Report.objects.all()
	return render(request, "reports.html", {"reports": reports})

def dashboard_metric_list(request):
	metrics = DashboardMetric.objects.all()
	return render(request, "dashboard_metrics.html", {"metrics": metrics})
