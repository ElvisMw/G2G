from django.db import models


from django.contrib.auth.models import User
import uuid

class UserProfile(models.Model):
	ROLE_CHOICES = [
		("ADMIN", "Admin"),
		("ACCOUNTANT", "Accountant"),
		("MANAGER", "Manager"),
		("VIEWER", "Viewer/Auditor"),
	]
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="VIEWER")
	phone_number = models.CharField(max_length=20, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} ({self.role})"
