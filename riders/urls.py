from django.urls import path
from .views import rider_list, rider_detail

urlpatterns = [
    path('', rider_list, name='rider_list'),
    path('<uuid:pk>/', rider_detail, name='rider_detail'),
]
