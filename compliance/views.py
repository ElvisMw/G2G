from django.shortcuts import render


from .models import ComplianceDocument

def compliance_list(request):
	documents = ComplianceDocument.objects.all()
	return render(request, "compliance.html", {"documents": documents})
