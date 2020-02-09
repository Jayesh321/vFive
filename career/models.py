from django.db import models
from django.urls import reverse
from django.contrib import auth
from employee.models import Profile
from django.contrib.auth.models import User



# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):
    
    def __str__(self):
        return self.username


class Job(models.Model):
    title=models.CharField(max_length=256)
    description=models.TextField()
    experience=models.IntegerField(default=0)
    location=models.CharField(default='Banglore', max_length=256)

    def get_absolute_url(self):
        return reverse('career:job_detail_url', kwargs={'pk':self.pk})


#superuser:
#user name=vFive
#password=vFive

class Contact(models.Model):
    firstname=models.CharField(max_length=256)
    lastname=models.CharField(max_length=256)
    email=models.EmailField()
    phone=models.IntegerField()
    textarea=models.TextField()

    def get_absolute_url(self):
        return reverse('contact_us')


# Model for  applying job:
class JobApply(Profile):
    phone = models.IntegerField(null='True')
    upload_file = models.FileField(upload_to='resume/pdfs', null='True')
    email = models.EmailField(null='True')
    experience = models.IntegerField(null='True')
    old_employee = models.CharField(max_length=20, null='True')

    def __str__(self):
        return self.phone 
