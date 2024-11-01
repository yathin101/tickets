# tickets/serializers.py
from rest_framework import serializers
from .models import Complaint, Ticket

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['id', 'title', 'description']

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'user', 'complaint', 'description', 'status', 'created_at', 'updated_at']
