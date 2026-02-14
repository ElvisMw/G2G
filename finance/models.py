from django.db import models
import uuid

class Remittance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	contract_id = models.UUIDField()
	rider_id = models.UUIDField()
	amount = models.DecimalField(max_digits=12, decimal_places=2)
	date = models.DateField()
	notes = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Remittance {self.amount} by {self.rider_id} on {self.date}"

class RevenueLog(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	vehicle_id = models.UUIDField()
	date = models.DateField()
	expected_revenue = models.DecimalField(max_digits=12, decimal_places=2)
	actual_revenue = models.DecimalField(max_digits=12, decimal_places=2)
	notes = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.vehicle_id} revenue on {self.date}"

class Payment(models.Model):
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		# Only update outstanding_balance for installment payments
		if self.payment_type == 'INSTALLMENT' and self.vehicle_id:
			from fleet.models import Vehicle
			try:
				vehicle = Vehicle.objects.get(id=self.vehicle_id)
				vehicle.outstanding_balance = vehicle.outstanding_balance - self.amount
				vehicle.save()
			except Vehicle.DoesNotExist:
				pass
	PAYMENT_TYPE_CHOICES = [
		("INSTALLMENT", "Installment"),
		("DEPOSIT", "Deposit"),
		("PENALTY", "Penalty"),
		("INSURANCE", "Insurance"),
		("SERVICE", "Service"),
		("REPAIR", "Repair"),
		("OTHER", "Other"),
	]

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	vehicle_id = models.UUIDField()
	contract_id = models.UUIDField()
	paid_from = models.CharField(max_length=255)
	paid_to = models.CharField(max_length=255)
	amount = models.DecimalField(max_digits=12, decimal_places=2)
	payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)
	mpesa_code = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=20)
	date_paid = models.DateTimeField()
	recorded_at = models.DateTimeField(auto_now_add=True)
	notes = models.TextField(blank=True, null=True)
	receipt_image = models.ImageField(upload_to='uploads/payments/', blank=True, null=True)

	def __str__(self):
		return f"{self.paid_from} paid {self.amount} to {self.paid_to} on {self.date_paid}" 
