from django.shortcuts import render # type: ignore

# Create your views here.

def courses(request): 

    return render(request, 'quiz/courses/courses.html' )