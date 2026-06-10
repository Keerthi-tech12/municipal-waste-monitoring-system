from django.db import models

class Vehicle(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Under Maintenance', 'Under Maintenance'),
        ('Inactive', 'Inactive'),
    ]

    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=100)
    capacity_kg = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.vehicle_number