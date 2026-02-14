from django.urls import path
from .views import compliance_list

urlpatterns = [
    path('', compliance_list, name='compliance_list'),
]
