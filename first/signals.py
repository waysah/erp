from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DailyWork,Employees, employee_initializer
from django.db import models
from django.db.models import Sum,  F, FloatField

@receiver(post_save, sender=DailyWork)
def update_total_income(sender, instance, created, **kwargs):
    if created:
        employee = instance.employee_ID
        total_income = employee.total_income + (instance.commision_rate / 100) * instance.total_amount
        employee.total_income = total_income
        employee.save()



