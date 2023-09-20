# Generated by Django 4.2.1 on 2023-05-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_employee_transaction_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='first_department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='addDepartment',
        ),
    ]
