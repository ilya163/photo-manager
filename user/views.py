from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

    
def userRegistration(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        checkUser = User.objects.filter(username=username).exists()
        if not checkUser:
            user = User.objects.create_user(username, username+"@gmail.com", password)
            user.save()
            messages.info(request, "Вы успешно зарегистрированы. Войдите на сайт")
            return redirect("home")
        else:
            messages.info(request, "Логин или пароль не соответствуют требованиям")
            return render(request, 'user/reg.html', {})
    else:
        return render(request, 'user/reg.html', {})


def userLogout(request):
    logout(request)
    messages.success(request, "Вы вышли из системы")
    return redirect('home')

def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
       
        if user is not None:
            login(request, user)
            return redirect("main")
        else: 
            messages.info(request, "Неверный логин или пароль")
            return render(request, 'user/login.html', {})
    else:
        return render(request, 'user/login.html', {})
