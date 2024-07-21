from django.urls import path # type: ignore
from . import views
urlpatterns = [
    path('', views.courses, name='courses')
    
]
