from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def userRegistration(request):
    """ Регистрирует пользователей на сайте """
    if request.method == "POST":
        context = {}
        is_success = False
        username = request.POST['username']
        password = request.POST['password']
        checkUser = User.objects.filter(username=username).exists()
        if checkUser:
            context["info"] = "Нельзя использовать существующий логин"
        elif len(username) < 4 or len(password) < 4:
            context["info"] = "Длина логина или пароля должна быть больше 3-х символов"
        else:
            is_success = True

        if is_success:
            user = User.objects.create_user(username, username + "@gmail.com", password)
            user.save()
            messages.success(request, "Вы успешно зарегистрированы")
            return redirect("home")
        else:
            return render(request, 'user/reg.html', context)
    else:
        return render(request, 'user/reg.html', {})


def userLogout(request):
    """ Завершает сессию пользователя """
    logout(request)
    messages.success(request, "Вы вышли из системы")
    return redirect('home')


def userLogin(request):
    """ Авторизовывает пользователя на сайте """
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Добро пожаловать - "+str(request.user))
            return redirect("main")
        else:
            context["info"] = "Неверный логин или пароль"
            return render(request, 'user/login.html', context)
    else:
        return render(request, 'user/login.html', {})
