from django import forms  # type: ignore

from .models import Questions



class QuestionForm(forms.ModelForm): 
    class Meta: 
        model = Questions
        fields = '__all__'
