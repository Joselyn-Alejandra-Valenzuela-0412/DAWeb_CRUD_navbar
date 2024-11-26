from django.urls import path
from app_base import views

urlpatterns = [
    #inicio comics PandaManga
    path('', views.inicio),
    
]
