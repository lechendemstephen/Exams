from django.shortcuts import render, redirect # type: ignore
from .forms import SignupForm, LoginForm
from .models import Signup
from django.contrib import messages # type: ignore
from django.contrib.auth import login, authenticate, logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth.hashers import check_password, make_password # type: ignore
# Create your views here.

def signup(request):
    if request.method == "POST": 
        form = SignupForm(request.POST)
        if form.is_valid(): 
           try: 
            name = form.cleaned_data['name']
            password = make_password(form.cleaned_data['password']) 
            user = Signup(
                name = name ,
                email = form.cleaned_data['email'],
                password = password,
                repeat_password = make_password(form.cleaned_data['repeat_password'])
            )
            user.save()
            user = authenticate(username= name, password=password )
            login(user)
            print('logged in')
            messages.success(request, 'Succesfully signed-Up')
            return redirect('courses')
           except: 
               pass
        else: 
           form = SignupForm()
        
    return render(request, 'quiz/accounts/signup.html' )


def login(request): 
    if request.method == "POST": 
        form = LoginForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user: 
                login(request, user)
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