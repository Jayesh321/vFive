# Generated by Django 2.2.6 on 2020-01-08 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=256)),
                ('lastname', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('textarea', models.TextField()),
            ],
        ),
    ]
