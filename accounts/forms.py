from django import forms  # type: ignore
from .models import Signup

class SignupForm(forms.ModelForm): 
    class Meta: 
        model = Signup
        fields = ('name', 'email', 'password', 'repeat_password')


class LoginForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ("name","password")
