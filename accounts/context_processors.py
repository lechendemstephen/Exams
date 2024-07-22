from .models import Signup

def user_name(request): 
    # creating an instance of the database 
    user = Signup.objects.filter()
    
    return  {
        'user_name': user,
    }