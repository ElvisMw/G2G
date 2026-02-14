from django.core.management.base import BaseCommand
from fleet.models import Vehicle
from finance.models import Payment
from django.db.models import Sum

class Command(BaseCommand):
    help = 'Recalculate outstanding_balance for all vehicles based on installment payments.'

    def handle(self, *args, **options):
        for vehicle in Vehicle.objects.all():
            total_installments = Payment.objects.filter(vehicle_id=vehicle.id, payment_type='INSTALLMENT').aggregate(total=Sum('amount'))['total'] or 0
            original_balance = vehicle.hire_purchase_price
            vehicle.outstanding_balance = original_balance - total_installments
            vehicle.save()
            self.stdout.write(self.style.SUCCESS(f'Updated {vehicle}: Outstanding = {vehicle.outstanding_balance}'))
        self.stdout.write(self.style.SUCCESS('All vehicle outstanding balances recalculated.'))
