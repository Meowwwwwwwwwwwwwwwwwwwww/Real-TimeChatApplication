from django.urls import path
from .views import *

urlpatterns = [
    path('', chatApp , name='home'),
    
]