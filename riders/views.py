from django.shortcuts import render


from .models import Rider

def rider_list(request):
	riders = Rider.objects.all()
	return render(request, "riders.html", {"riders": riders})

def rider_detail(request, pk):
	rider = Rider.objects.get(pk=pk)
	return render(request, "rider_detail.html", {"rider": rider})
