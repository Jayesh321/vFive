# Generated by Django 2.2.6 on 2020-01-16 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0004_auto_20200116_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=0),
        ),
    ]
