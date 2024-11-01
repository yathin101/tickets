from django.contrib import admin
from .models import Complaint, Ticket

# Register Complaint model
@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']

# Register Ticket model
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'complaint', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__username', 'complaint__title', 'description']
    ordering = ['-created_at']
