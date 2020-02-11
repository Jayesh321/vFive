from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, TemplateView)
from . import forms

# Create your views here.
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

class SignUpView(CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

