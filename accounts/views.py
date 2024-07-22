from django.shortcuts import render, redirect # type: ignore
from .forms import SignupForm, LoginForm
from .models import Signup
from django.contrib import messages # type: ignore
from django.contrib.auth import login, authenticate, logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
# Create your views here.

def signup(request): 
    if request.method == "POST": 
        form = SignupForm(request.POST)

        if form.is_valid(): 
            user = Signup(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
                repeat_password = form.cleaned_data['repeat_password']
            )
            user.save()
            user = authenticate(username= form.cleaned_data['name'], password=form.cleaned_data['password'] )
            login(user)

            messages.success(request, 'Succesfully signed-Up')
            return redirect('courses')
        else: 
            form = SignupForm()
        
    return render(request, 'quiz/accounts/signup.html' )


def login(request): 
    if request.method == "POST": 
        form = LoginForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # creating an instance of the Signup
            user = Signup.objects.filter()
            if user.name == username and user.password == password: 
                print('Login')
                return redirect('home')
    else: 
        form = LoginForm

    return render(request, 'quiz/accounts/signin.html' )


@login_required(login_url='login')
def log_out(request):
    logout(request) 
    messages.success(request, 'Logout sucessfull')
    return redirect('home')