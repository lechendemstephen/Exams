from django.shortcuts import render, redirect # type: ignore
from .forms import SignupForm, LoginForm
from django.contrib import messages, auth# type: ignore
from django.contrib.auth import login, authenticate, logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth.hashers import check_password, make_password # type: ignore
from .models import User

# Create your views here.

def signup(request):
    if request.method == "POST": 
        form = SignupForm(request.POST)
        if form.is_valid(): 
            try: 
                first_name =form.cleaned_data['first_name']
                last_name  =form.cleaned_data['last_name']
                email      =form.cleaned_data['email']
                password   =form.cleaned_data['password']
                confirm_password =form.cleaned_data['confirm_password']
                if confirm_password != password: 
                    messages.error(request, "password and confirm password don't mstch" )
                else:
                    user = User.objects.create_user(
                        first_name = first_name,
                        last_name = last_name,
                        email = email, 
                        password = password, 
                    )
                    user.save()
                    user = authenticate(email=email, password=password)
                    login(user)
                    messages.success(request, 'Account sucessfully created')
                    return redirect('home')
            except: 
                pass
        
        else: 
           form = SignupForm()
        
    return render(request, 'quiz/accounts/signup.html' )


def login(request): 
    if request.method == "POST": 
        form = LoginForm(request.POST)
        if form.is_valid(): 
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email= email, password = password)
            if user is not None: 
                login(user)
                print('login successfull')
                return redirect('home') 
    else: 
        form = LoginForm()
             
    return render(request, 'quiz/accounts/signin.html' )


@login_required(login_url='login')
def log_out(request):
    logout(request) 
    messages.success(request, 'Logout sucessfull')
    return redirect('home')