from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.forms import modelformset_factory

from .forms import ImageForm
from .models import Image


from datetime import datetime
from django.utils import timezone

@login_required  
def mainContent(request):

    images = Image.objects.all().filter(reporter=request.user)
    sort = "asc"
    if request.method == 'GET':
        if request.GET.get("sort") == "asc":
            images = Image.objects.filter(reporter=request.user).order_by("title")
            sort = "desc"
        elif request.GET.get("sort") == "desc":
            images = Image.objects.filter(reporter=request.user).order_by("-title")
            sort = "asc"

    context = {
        "images": images,
        "sort": sort
    }
    return render(request, "main/main.html", context)

def removeImage(request, id):
    rm = get_object_or_404(Image, id=id)
    if rm.image_url:
        rm.image_url.delete()
    rm.delete()
    return redirect("main")



def uploadImage(request):
    if request.method == 'POST':
        # question = get_object_or_404(Image, pk=2)
        imageModel = Image(pub_date=timezone.now(), reporter=request.user)
        form = ImageForm(request.POST, request.FILES, instance=imageModel)
        if form.is_valid():
            form.save()
            messages.info(request, "Ваше фото загружено")
            return redirect("main")
        else:
            form["error"]= "Ошибка при валидации формы"
            return render(request, "main/upload_image.html", {"form": form})
    else:
        form = ImageForm()
        context = {
         "form": form,
        }
        return render(request, "main/upload_image.html", context)