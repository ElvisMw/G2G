
import uuid
from django.db import models

class DowntimeLog(models.Model):
	REASON_CHOICES = [
		("MECHANICAL", "Mechanical"),
		("MAINTENANCE", "Maintenance"),
		("ACCIDENT", "Accident"),
		("REGULATORY", "Regulatory"),
		("PERSONAL_LEAVE", "Personal Leave"),
		("OTHER", "Other"),
	]
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	vehicle_id = models.UUIDField()
	start_date = models.DateField()
	end_date = models.DateField(blank=True, null=True)
	reason = models.CharField(max_length=32, choices=REASON_CHOICES)
	notes = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.vehicle_id} - {self.reason} from {self.start_date}"

class MaintenanceRecord(models.Model):
	CATEGORY_CHOICES = [
		("FUEL", "Fuel"),
		("REPAIR", "Repair"),
		("SPARE_PART", "Spare Part"),
		("INSURANCE", "Insurance"),
		("LICENSE", "License"),
		("PENALTY", "Penalty"),
		("OTHER", "Other"),
	]

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	vehicle_id = models.UUIDField()
	date = models.DateField()
	category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
	description = models.TextField()
	amount = models.DecimalField(max_digits=12, decimal_places=2)
	receipt_image = models.ImageField(upload_to='uploads/maintenance/', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.vehicle_id} - {self.category} on {self.date}"

import uuid

class OdometerLog(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	vehicle_id = models.UUIDField()
	date = models.DateField()
	mileage = models.PositiveIntegerField()
	notes = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.vehicle_id} - {self.mileage} km on {self.date}"

class ServiceRecord(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	vehicle_id = models.UUIDField()
	service_type = models.CharField(max_length=64)
	mechanic = models.CharField(max_length=128)
	service_date = models.DateField()
	next_service_due = models.DateField(blank=True, null=True)
	cost = models.DecimalField(max_digits=12, decimal_places=2)
	receipt_image = models.ImageField(upload_to='uploads/maintenance/services/', blank=True, null=True)
	notes = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.vehicle_id} - {self.service_type} on {self.service_date}"

class ComponentRecord(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	vehicle_id = models.UUIDField()
	component_name = models.CharField(max_length=128)
	supplier = models.CharField(max_length=128)
	warranty_expiry = models.DateField(blank=True, null=True)
	purchase_date = models.DateField()
	cost = models.DecimalField(max_digits=12, decimal_places=2)
	failure_frequency = models.PositiveIntegerField(default=0)
	mechanic = models.CharField(max_length=128, blank=True, null=True)
	receipt_image = models.ImageField(upload_to='uploads/maintenance/components/', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.vehicle_id} - {self.component_name}"
