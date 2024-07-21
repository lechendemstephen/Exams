from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('question/', views.question, name='question'),

    path('', views.home, name='home' ),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]
