from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import JsonResponse
from django.contrib import messages

from .forms import ImageForm
from .models import Image


@csrf_exempt
@login_required
def mainContent(request):
    """ Отображение контента галереи"""
    images = Image.objects.all().filter(reporter=request.user)
    sort = "asc"
    if request.method == 'GET':
        if request.GET.get("sort") == "asc":
            images = Image.objects.filter(reporter=request.user).order_by("title")
            sort = "desc"
        elif request.GET.get("sort") == "desc":
            images = Image.objects.filter(reporter=request.user).order_by("-title")
            sort = "asc"
    if request.method == "POST":
        return JsonResponse({"title": request.POST.get("filter_title")})
    context = {
        "images": images,
        "sort": sort,
    }
    return render(request, "main/main.html", context)


def removeImage(request, id):
    """ Удаляет картинку из фотогаллереи"""
    rm = get_object_or_404(Image, id=id)
    if rm.image_url:
        rm.image_url.delete()
    rm.delete()
    return redirect("main")


def uploadImage(request):
    """ Загружает новое фото в галерею """
    if request.method == 'POST':
        imageModel = Image(pub_date=timezone.now(), reporter=request.user)
        form = ImageForm(request.POST, request.FILES, instance=imageModel)
        if form.is_valid():
            form.save()
        else:
            messages.error("Ошибка при валидации формы")
        return redirect('main')
    else:
        form = ImageForm()
        return render(request, "main/upload_image.html", {"form": form})
