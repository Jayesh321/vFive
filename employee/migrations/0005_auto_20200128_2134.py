# Generated by Django 3.0.2 on 2020-01-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20200128_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='father_dob',
            field=models.DateField(blank=True, null='True'),
        ),
    ]
