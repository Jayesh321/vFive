from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView)
from employee.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
class ProfileView(LoginRequiredMixin,TemplateView):
    model = Profile
    template_name = 'employee/profile.html'
    login_url = '/career/login/'
    #redirect_field_name = 'redirect_to'
    

#class ProfileList(ListView):
    #model = Profile

#class ProfileDetailView(DetailView):
    #model = Profile
    