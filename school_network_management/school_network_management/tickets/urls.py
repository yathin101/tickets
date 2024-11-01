# tickets/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComplaintViewSet, TicketViewSet

router = DefaultRouter()
router.register(r'complaints', ComplaintViewSet, basename='complaint')
router.register(r'tickets', TicketViewSet, basename='ticket')

urlpatterns = [
    path('', include(router.urls)),
]
