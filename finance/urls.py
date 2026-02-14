from django.urls import path
from .views import payment_list, remittance_list, revenue_log_list

urlpatterns = [
    path('', payment_list, name='payment_list'),
    path('remittances/', remittance_list, name='remittance_list'),
    path('revenue-logs/', revenue_log_list, name='revenue_log_list'),
]
