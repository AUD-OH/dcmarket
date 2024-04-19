from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    first_name = forms.CharField(label='First Name', widget=forms.TextInput())
    family_name = forms.CharField(label='Family Name', widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'family_name', 'email',)
