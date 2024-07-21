from django.shortcuts import render # type: ignore

# Create your views here.

def signup(request): 

    return render(request, 'quiz/accounts/signup.html' )


def login(request): 

    return render(request, 'quiz/accounts/signin.html' )