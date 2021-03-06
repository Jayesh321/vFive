# Generated by Django 3.0.2 on 2020-01-29 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_profile_full_name'),
        ('career', '0006_jobapply'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapply',
            name='email',
            field=models.EmailField(max_length=254, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='jobapply',
            name='experience',
            field=models.IntegerField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='jobapply',
            name='old_employee',
            field=models.CharField(max_length=20, null='True'),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='phone',
            field=models.IntegerField(null='True'),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='profile_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employee.Profile'),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='upload_file',
            field=models.FileField(null='True', upload_to='resume/pdfs'),
        ),
    ]
