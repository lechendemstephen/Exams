from django.contrib import admin # type: ignore
from .models import Signup
# Register your models here.

class SignupAdmin(admin.ModelAdmin): 
    list_display = ('name', 'email', 'password', 'repeat_password', 'jioned_date')


admin.site.register(Signup, SignupAdmin)