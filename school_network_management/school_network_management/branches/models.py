# branches/models.py
from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.zone} - {self.name}"

class ServiceProvider(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="providers")
    isp_provider = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    account_type = models.CharField(max_length=20, choices=[('Broadband', 'Broadband'), ('Leased', 'Leased'), ('Semi Leased', 'Semi Leased')])
    speed = models.CharField(max_length=20)
    ppoe_username = models.CharField(max_length=50)
    ppoe_password = models.CharField(max_length=50)
    static_ip = models.GenericIPAddressField(null=True, blank=True)
    subnet_mask = models.CharField(max_length=50, null=True, blank=True)
    gateway = models.CharField(max_length=50, null=True, blank=True)
    dns1 = models.CharField(max_length=50, null=True, blank=True)
    dns2 = models.CharField(max_length=50, null=True, blank=True)
    local_ip = models.CharField(max_length=50, null=True, blank=True)
    vpn_type = models.CharField(max_length=20, choices=[('IPSEC', 'IPSEC'), ('SSL', 'SSL')], null=True, blank=True)
    ssl_username = models.CharField(max_length=50, null=True, blank=True)
    ssl_password = models.CharField(max_length=50, null=True, blank=True)
    billing_type = models.CharField(max_length=20, choices=[('Quarterly', 'Quarterly'), ('Monthly', 'Monthly'), ('Off Yearly', 'Off Yearly'), ('Yearly', 'Yearly')])
    monthly_charges = models.DecimalField(max_digits=10, decimal_places=2)
    engineer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.isp_provider} for {self.branch.name}"
