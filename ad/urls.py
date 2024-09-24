from django.urls import path
from . import views

urlpatterns = [
    path('', views.Ad, name='ad_create'),
]