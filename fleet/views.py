from django.shortcuts import render


from .models import Vehicle

def vehicle_list(request):
	vehicles = Vehicle.objects.all()
	return render(request, "vehicles.html", {"vehicles": vehicles})

def vehicle_detail(request, pk):
	vehicle = Vehicle.objects.get(pk=pk)
	return render(request, "vehicle_detail.html", {"vehicle": vehicle})
