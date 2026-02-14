from django.db import models


import uuid

class Report(models.Model):
	REPORT_TYPE_CHOICES = [
		("VEHICLE_FINANCIAL", "Vehicle Financial Report"),
		("MONTHLY_PROFIT", "Monthly Profit Report"),
		("ANNUAL_SUMMARY", "Annual Summary"),
		("RIDER_STATEMENT", "Rider Statement"),
		("HIRE_PURCHASE_STATEMENT", "Hire Purchase Statement"),
		("MAINTENANCE_SUMMARY", "Maintenance Summary"),
		("COMPLIANCE_REPORT", "Compliance Report"),
		("CONTRACT_AGREEMENT", "Contract Agreement"),
		("EXPENSE_SUMMARY", "Expense Summary"),
		("FLEET_PERFORMANCE", "Fleet Performance Report"),
	]
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	report_type = models.CharField(max_length=32, choices=REPORT_TYPE_CHOICES)
	generated_for = models.CharField(max_length=128, blank=True, null=True)
	generated_at = models.DateTimeField(auto_now_add=True)
	file = models.FileField(upload_to='uploads/reports/', blank=True, null=True)

	def __str__(self):
		return f"{self.get_report_type_display()} ({self.generated_at.date()})"

class DashboardMetric(models.Model):
	METRIC_TYPE_CHOICES = [
		("TOTAL_FLEET_VALUE", "Total Fleet Value"),
		("OUTSTANDING_LIABILITIES", "Outstanding Liabilities"),
		("MONTHLY_REVENUE", "Monthly Revenue"),
		("NET_PROFIT", "Net Profit"),
		("MOST_PROFITABLE_VEHICLE", "Most Profitable Vehicle"),
		("HIGHEST_MAINTENANCE_VEHICLE", "Highest Maintenance Vehicle"),
		("COMPLIANCE_ALERTS", "Compliance Alerts"),
		("CONTRACT_EXPIRY_ALERTS", "Contract Expiry Alerts"),
	]
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	metric_type = models.CharField(max_length=32, choices=METRIC_TYPE_CHOICES)
	value = models.CharField(max_length=128)
	calculated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.get_metric_type_display()}: {self.value}"
