from django.contrib import admin # type: ignore
from django.contrib.auth.admin import UserAdmin # type: ignore
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin): 
    list_display = ('first_name', 'last_name', 'username', 'email', 'password', 'date_jioned')

   
admin.site.register(User, UserAdmin)
