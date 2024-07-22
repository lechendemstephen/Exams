from django.urls import path # type: ignore
from . import views
urlpatterns = [
    path('sign-up/', views.signup, name='signup'),
    path('sign-in/', views.login, name='login'),
    path('logout/', views.log_out, name="logout"),
]
