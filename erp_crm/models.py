from django.db import models

# Create your models here.
# models.py

class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    services_ordered = models.ManyToManyField(Service, blank=True)
    payments = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def total_due(self):
        return sum(service.price for service in self.services_ordered.all())
