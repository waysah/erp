# Generated by Django 4.2.1 on 2023-06-30 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0032_alter_manager_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='employee_lever',
            field=models.CharField(choices=[('CEO', 'CEO'), ('MANAGER', 'Manager')], max_length=100),
        ),
    ]
