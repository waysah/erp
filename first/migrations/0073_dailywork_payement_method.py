# Generated by Django 4.0.6 on 2023-08-10 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0072_alter_dailywork_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailywork',
            name='Payement_method',
            field=models.CharField(blank=True, choices=[('M-PESA', 'm-pesa'), ('CASH', 'cash')], max_length=255, null=True),
        ),
    ]