from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as BaseUserChangeForm
from users.models import User


class UserCreationForm(BaseUserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
            'username': 'Carnet',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Email'
        }


class UserChangeForm(BaseUserChangeForm):

    class Meta:
        model = User
        fields = ('email',)
