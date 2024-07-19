from django.db import models # type: ignore

# Create your models here.

class Questions(models.Model): 
    question = models.CharField(max_length=200, null=True)
    optionA  = models.CharField(max_length=200,  null=True)
    optionB  = models.CharField(max_length=200,  null=True)
    optionC  = models.CharField(max_length=200,  null=True)
    optionD  = models.CharField(max_length=200,  null=True)
    answer   =  models.CharField(max_length=200,  null=True)

    class Meta: 
        verbose_name = 'Questions'
        verbose_name_plural = 'Questions'


    def __str__(self): 

        return self.question 
    

    