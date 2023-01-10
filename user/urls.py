from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.userRegistration, name="reg"),
    path('login/', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
    ]