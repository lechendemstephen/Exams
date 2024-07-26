from django import forms  # type: ignore
from .models import User

class SignupForm(forms.ModelForm): 
    class Meta: 
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "password")
