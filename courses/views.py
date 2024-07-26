from django.shortcuts import render # type: ignore
# Create your views here.

def courses(request): 
    context = {
        'courses': "active",
    }

    return render(request, 'quiz/courses/courses.html', context)