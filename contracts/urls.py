from django.urls import path
from .views import contract_list, contract_detail

urlpatterns = [
    path('', contract_list, name='contract_list'),
    path('<uuid:pk>/', contract_detail, name='contract_detail'),
]
