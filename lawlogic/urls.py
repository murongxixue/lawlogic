from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *
app_name = 'lawlogic'

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    
]