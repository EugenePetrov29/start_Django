from django.shortcuts import render
from django.contrib.auth import views
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from . import models
from . import forms
from .forms import LoginForm, UserRegistrationForm
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'accs/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accs/register.html', {'user_form': user_form})
# Create your views here.

class LoginView(views.LoginView):
    template_name = 'accs/login.html'

class Profile(CreateView):
    template_name = 'accs/user_form.html'
    model = models.Profile
    form_class = forms.RegisterForm
    success_url = "/"
    

class Logout(views.LogoutView):
    template_name = ''
    
class ProfileDetail(DetailView):
    template_name = 'accs/profile_detail.html'
    model = models.Profile

class ProfileUpdate(UpdateView):
    model = models.Profile
    template_name = 'accs/profile_update.html'
    fields = (
        'phone',
        'address',
        'birth_date',
        )
    
    
    def get_success_url(self):
        return reverse('profile_detail', args=[self.kwargs['pk']])
    