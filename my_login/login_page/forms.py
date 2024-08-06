# forms.py
from django import forms
from .models import User

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class CreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','text']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
