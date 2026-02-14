from django.shortcuts import render


from .models import UserProfile

def userprofile_list(request):
	userprofiles = UserProfile.objects.all()
	return render(request, "userprofiles.html", {"userprofiles": userprofiles})
