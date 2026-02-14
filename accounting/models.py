

import uuid
from django.db import models

class AuditLog(models.Model):
	ACTION_CHOICES = [
		("CREATE", "Create"),
		("UPDATE", "Update"),
		("DELETE", "Delete"),
		("POST", "Post"),
	]
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user_id = models.UUIDField()
	action = models.CharField(max_length=10, choices=ACTION_CHOICES)
	model_name = models.CharField(max_length=64)
	object_id = models.UUIDField()
	timestamp = models.DateTimeField(auto_now_add=True)
	details = models.TextField(blank=True, null=True)

	def __str__(self):
		return f"{self.action} on {self.model_name} by {self.user_id} at {self.timestamp}"


import uuid

class Account(models.Model):
	ACCOUNT_TYPE_CHOICES = [
		("ASSET", "Asset"),
		("LIABILITY", "Liability"),
		("EQUITY", "Equity"),
		("INCOME", "Income"),
		("EXPENSE", "Expense"),
	]
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=64, unique=True)
	account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name

class JournalEntry(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	date = models.DateField()
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	description = models.TextField()
	debit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
	credit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
	balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	is_deleted = models.BooleanField(default=False)
	immutable = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.date} - {self.account.name}"
