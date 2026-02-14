from django.db import models


import uuid

class Contract(models.Model):
	REVENUE_MODEL_CHOICES = [
		("FIXED", "Fixed Daily Remittance"),
		("PERCENTAGE", "Percentage Share"),
		("HYBRID", "Hybrid"),
	]
	STATUS_CHOICES = [
		("ACTIVE", "Active"),
		("INACTIVE", "Inactive"),
		("TERMINATED", "Terminated"),
	]

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	vehicle_id = models.UUIDField()
	rider_id = models.UUIDField()
	start_date = models.DateField()
	end_date = models.DateField(blank=True, null=True)
	revenue_model = models.CharField(max_length=20, choices=REVENUE_MODEL_CHOICES)
	security_deposit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
	terms = models.TextField()
	contract_file = models.FileField(upload_to='uploads/contracts/', blank=True, null=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ACTIVE")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"Contract {self.id} for Vehicle {self.vehicle_id}"
