from django.shortcuts import render
from django.views.generic import (TemplateView, FormView, CreateView)
from career.models import Contact
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class ContactView(CreateView):
    template_name='contact_us.html'
    model=Contact
    fields=['firstname', 'lastname', 'email', 'phone', 'textarea']

class AboutView(TemplateView):
    template_name='about_us.html'



