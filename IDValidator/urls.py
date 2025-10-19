from django.urls import path
from .views import CheckID

urlpatterns = [
    path('CheckID/',CheckID , name= 'check national id'),
]