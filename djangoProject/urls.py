
from django.contrib import admin
from django.urls import path
from blog import views

import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djbbs.settings')
django.setup()

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/',views.LoginView.as_view()),
    path('login/',views.login),
    path('res/',views.res)
]
