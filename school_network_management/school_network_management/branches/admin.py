# branches/admin.py
from django.contrib import admin
from .models import Branch, ServiceProvider

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'zone', 'name')
    search_fields = ('zone', 'name')

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'branch', 'isp_provider', 'account_number', 'account_type',
        'speed', 'ppoe_username', 'static_ip', 'vpn_type', 'billing_type',
        'monthly_charges', 'engineer'
    )
    list_filter = ('branch', 'account_type', 'billing_type', 'vpn_type')
    search_fields = ('isp_provider', 'account_number', 'engineer')
