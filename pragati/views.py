from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import (CreateView, ListView, TemplateView, DetailView)
from pragati.models import Idea

# Create your views here.
class HomeView(TemplateView):
    template_name = 'pragati/home.html'

class IdeaListView(ListView):
    model = Idea
    #ordering = ['-date_posted'] 

class IdeaCreateView(CreateView):
    model = Idea
    template_name = 'pragati/idea_form.html'
    fields = ['idea', 'save_time', 'save_money', 'save_effort']

class IdeaDetailView(DetailView):
    model = Idea
    template_name = 'pragati/idea_detail.html'


def Idea_Like(request):
    idea = get_object_or_404(Idea, id=request.POST.get('idea_id'))
    idea.Likes.add(request.user)
    return HttpResponseRedirect(idea.get_absolute_url())