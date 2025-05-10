from django.urls import path
from .views import *

urlpatterns = [
    path('',receiver,name='receiver'),
    
]