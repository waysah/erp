# Generated by Django 4.2.1 on 2023-08-16 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0078_system_payment_system_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='payement_gateway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='system_payment',
            name='Amount',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='system_payment',
            name='payment_method',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='system_update',
            name='company_logo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='system_update',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
