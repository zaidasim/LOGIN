# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
    text = forms.CharField(label='Text', widget=forms.PasswordInput)
