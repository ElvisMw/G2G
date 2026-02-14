from django.db import models


import uuid

class ComplianceDocument(models.Model):
	STATUS_CHOICES = [
		("VALID", "Valid"),
		("EXPIRED", "Expired"),
		("PENDING", "Pending"),
	]

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=64)
	number = models.CharField(max_length=64)
	vehicle_id = models.UUIDField()
	issue_date = models.DateField()
	expiry_date = models.DateField()
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="VALID")
	file_url = models.FileField(upload_to='uploads/compliance/', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.name} for {self.vehicle_id}"
