from django.urls import path
from .views import vehicle_list, vehicle_detail

urlpatterns = [
    path('', vehicle_list, name='vehicle_list'),
    path('<uuid:pk>/', vehicle_detail, name='vehicle_detail'),
]
