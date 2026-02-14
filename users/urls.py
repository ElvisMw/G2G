from django.urls import path
from .views import userprofile_list

urlpatterns = [
    path('', userprofile_list, name='userprofile_list'),
]
