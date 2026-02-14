from django.urls import path
from .views import report_list, dashboard_metric_list

urlpatterns = [
    path('', report_list, name='report_list'),
    path('dashboard-metrics/', dashboard_metric_list, name='dashboard_metric_list'),
]
