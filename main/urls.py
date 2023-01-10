from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.mainContent, name="main"),
    path('upload_image', views.uploadImage, name="upload_image"),
    path('remove_image/<int:id>', views.removeImage, name="remove_image"),
    path('sort_image_title/', views.removeImage, name="remove_image"),
]
