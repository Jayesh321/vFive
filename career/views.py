from django.shortcuts import render, redirect
from django.views.generic import (ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView)
from career.models import (Job, JobApply)
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from career.forms import UserRegisterationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
''' 
def RegistrationView(request):
    if request.method == "POST":
        form=UserRegisterationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {username}!')
            return redirect ('index')

    else:
        form =  UserRegisterationForm()

    return render(request, 'career/registration.html', {'form':form})'''



# Career Application:

class JobList(ListView):
    model = Job

class JobDetailView(PermissionRequiredMixin, DetailView):
    model = Job
    permission_required = ('career.view_job')
    login_url = '/career/login/'

class CreateJobView(PermissionRequiredMixin, CreateView):
    model = Job
    fields = ['title', 'description', 'experience', 'location']
    permission_required = ( 'career.add_job' )

class UpdateJobView(PermissionRequiredMixin, UpdateView):
    model = Job
    fields = ['title', 'description', 'experience', 'location']
    permission_required = ( 'career.change_job' )

class DeleteJobView(PermissionRequiredMixin, DeleteView):
    model = Job
    success_url =reverse_lazy('career:all')
    permission_required = ( 'career.delete_job' )

class CreateJobApplyView(PermissionRequiredMixin, CreateView):
    model = JobApply
    fields = ['full_name','email','country','experience','old_employee']
    permission_required = ('career.add_jobapply')


def upload(request, PermissionRequiredMixin):
    if request == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)

    return render(request, "career/jobapply.html")


    



