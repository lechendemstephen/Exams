from django.shortcuts import render, redirect # type: ignore
from .models import Questions
from .forms import QuestionForm
# Create your views here.

#______________________________________________________________________________________
def question(request):
    if request.method == 'POST':
        questions=Questions.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            if q.answer ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'quiz/pages/result.html',context)
    else:
        questions=Questions.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'quiz/pages/question.html',context)

# home
#_____________________________________________________________________________
def home(request): 


    return render(request, 'quiz/pages/home.html')

#about 
# ________________________________________________________________________________
def about(request): 

    return render(request, 'quiz/pages/about.html' )

# contact
# _______________________________________________________________________
def contact(request): 

    return render(request, 'quiz/pages/contact.html' )