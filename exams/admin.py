from django.contrib import admin # type: ignore
from .models import Questions
# Register your models here.

class QuestionsAdmin(admin.ModelAdmin): 
    list_display = ('question', 'optionA', 'optionB', 'optionC', 'optionD', 'answer')



admin.site.register(Questions, QuestionsAdmin)