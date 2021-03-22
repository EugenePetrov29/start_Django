from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class LoginForm(forms.Form):
    username = forms.CharField(
        label='username',
        required=True
    )
    password = forms.CharField(
        label='password',
        required=True,
        widget=forms.HiddenInput
    )

class RegisterForm(forms.ModelForm):        
    class Meta:
        model = Profile
        fields = (
        'user',
        'phone',
        'address',
        'birth_date'
        )
        initial = {
            'user': User.username, # This field value will be shown in the form when an unbound form is loaded.
        }
        