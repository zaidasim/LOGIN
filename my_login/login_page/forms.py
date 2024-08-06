# forms.py
from django import forms
from .models import User
from django.contrib.auth import get_user_model
class CreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','text']



class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email']
