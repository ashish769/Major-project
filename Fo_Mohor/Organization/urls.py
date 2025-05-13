from django.urls import path
from . import views

urlpatterns = [
    path('requests/', views.requests_view, name='requests'),
    path('route/', views.route_view, name='route'),
    path('receiver_profile/', views.profile_view, name='receiver_profile'),
    
]
