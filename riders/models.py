from django.db import models


import uuid

class Rider(models.Model):
	STATUS_CHOICES = [
		("ACTIVE", "Active"),
		("INACTIVE", "Inactive"),
	]

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	national_id = models.CharField(max_length=32, unique=True)
	phone_number = models.CharField(max_length=20)
	passport_photo = models.ImageField(upload_to='uploads/riders/photos/', blank=True, null=True)
	license_document = models.FileField(upload_to='uploads/riders/licenses/', blank=True, null=True)
	id_copy = models.FileField(upload_to='uploads/riders/id_copies/', blank=True, null=True)
	assigned_vehicle = models.UUIDField(blank=True, null=True)
	assignment_history = models.JSONField(blank=True, null=True, help_text="List of previous vehicle assignments")
	compliance_history = models.JSONField(blank=True, null=True, help_text="List of compliance events or issues")
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ACTIVE")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"
