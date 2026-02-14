from django.db import models


import uuid

class Vehicle(models.Model):
	STATUS_CHOICES = [
		("ACTIVE", "Active"),
		("INACTIVE", "Inactive"),
		("UNDER_REPAIR", "Under Repair"),
		("RETIRED", "Retired"),
	]

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	registration_number = models.CharField(max_length=32, unique=True)
	make = models.CharField(max_length=64)
	model = models.CharField(max_length=64)
	engine_number = models.CharField(max_length=64, blank=True, null=True)
	chassis_number = models.CharField(max_length=64, blank=True, null=True)
	actual_price = models.DecimalField(max_digits=12, decimal_places=2)
	hire_purchase_price = models.DecimalField(max_digits=12, decimal_places=2)
	deposit_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0)
	monthly_installment = models.DecimalField(max_digits=12, decimal_places=2)
	installment_period = models.PositiveIntegerField(help_text="Number of months")
	outstanding_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ACTIVE")
	image = models.ImageField(upload_to='uploads/vehicles/', blank=True, null=True)

	# Performance and risk tracking
	total_kilometers = models.PositiveIntegerField(default=0)
	in_service_days = models.PositiveIntegerField(default=0)
	off_days = models.PositiveIntegerField(default=0)
	risk_assessment = models.TextField(blank=True, null=True)
	asset_recovery_status = models.CharField(max_length=64, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.registration_number} - {self.make} {self.model}"
