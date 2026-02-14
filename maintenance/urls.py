from django.urls import path
from .views import maintenance_list, odometer_log_list, service_record_list, component_record_list, downtime_log_list

urlpatterns = [
    path('', maintenance_list, name='maintenance_list'),
    path('odometer-logs/', odometer_log_list, name='odometer_log_list'),
    path('service-records/', service_record_list, name='service_record_list'),
    path('component-records/', component_record_list, name='component_record_list'),
    path('downtime-logs/', downtime_log_list, name='downtime_log_list'),
]
