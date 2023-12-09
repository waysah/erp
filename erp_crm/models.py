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
    
class Payment(models.Model):
    Amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=255, null=True, blank=True)

class Payment_Record_Status(models.Model):
    remaining_amount = models.PositiveIntegerField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
