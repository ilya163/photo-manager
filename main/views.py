
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from .forms import ImageForm
from .models import Image

from django.utils import timezone
from django.http import JsonResponse

@csrf_exempt
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

    if request.method == "POST":
        return JsonResponse({"title": request.POST.get("filter_title")})

    context = {
        "images": images,
        "sort": sort,
     }

    print(context)
    return render(request, "main/main.html", context)

# def getFilterTitle(self, **kwargs):
#     context = super().getFilterTitle(**kwargs)
#     images = Image.objects.all()
#     context["filter_title"] = json.dumps(images)
#     return context
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
            form["error"] = "Ошибка при валидации формы"
            return render(request, "main/upload_image.html", {"form": form})
    else:
        form = ImageForm()
        context = {
         "form": form,
        }
        return render(request, "main/upload_image.html", context)