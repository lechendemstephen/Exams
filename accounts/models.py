from django.db import models # type: ignore
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin # type: ignore
# Create your models here.
class CustomerUserManager(BaseUserManager): 
    def create_user(self, first_name, last_name, email, password=None): 
        if not email: 
            raise ValueError('User must have email address')
      
        user = self.model(
            email = self.normalize_email(email),
           
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self, first_name, last_name, email, username, password): 
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)

        return user 
       

class User(AbstractBaseUser, PermissionsMixin): 
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=150, blank=False, default='', unique=True)
   

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)


    date_jioned = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    objects = CustomerUserManager()


    class Meta: 
        verbose_name = 'Users'
        verbose_name_plural = 'Users'

    def get_full_name(self): 

        return self.name
    
    def get_short_name(self): 
        return self.name or self.email.split('@')[0]
    
    def has_perm(self, perm, obj=None): 
        return self.is_admin
    





