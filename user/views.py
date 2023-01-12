from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

    
def userRegistration(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        checkUser = User.objects.filter(username=username).exists()
        if not checkUser:
            user = User.objects.create_user(username, username+"@gmail.com", password)
            user.save()
            context["info"] = "Вы успешно зарегистрированы. Войдите на сайт"
            return render(request, 'mymanager/home.html', context)
        elif len(username) > 3 and len(password) > 3:
            context["info"] = "Длина логина или пароля должна быть больше 3-х символов"
        else:
            context["info"] = "Нельзя использовать существующий логин"
        return render(request, 'user/reg.html', context)
    else:
        return render(request, 'user/reg.html', {})


def userLogout(request):
    logout(request)
    messages.success(request, "Вы вышли из системы")
    return redirect('home')

def userLogin(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
       
        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            context["info"] = "Неверный логин или пароль"
            return render(request, 'user/login.html', context)
    else:
        return render(request, 'user/login.html', {})
