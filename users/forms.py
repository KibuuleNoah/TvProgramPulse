from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    User creation form or user signup form
    for creating a new user
    """

    class Meta:
        model = CustomUser
        fields = ["username"]


class CustomUserChangeForm(UserChangeForm):
    """
    User change form or user update form used to
    change user information
    """

    class Meta:
        model = CustomUser
        fields = ["username"]


class UserLoginForm(forms.Form):
    """
    User login form that is used to authenticate a user
    """

    username = forms.CharField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput)
