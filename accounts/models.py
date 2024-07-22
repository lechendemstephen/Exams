from django.db import models # type: ignore

# Create your models here.
class Signup(models.Model): 
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    repeat_password = models.CharField(max_length=100)
    jioned_date = models.DateTimeField(auto_now_add=True)



    def __str__(self): 

        return self.name