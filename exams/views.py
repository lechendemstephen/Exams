from django.shortcuts import render # type: ignore
from .models import Questions
# Create your views here.

def home(request): 
    q = Questions.objects.all()



    context = {
        'questions': q
    }


    return render(request, 'quiz/pages/home.html', context)