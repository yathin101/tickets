# branches/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.branch_list, name='branch_list'),
    path('branch/<int:branch_id>/add/', views.service_provider_form, name='service_provider_form'),
]
