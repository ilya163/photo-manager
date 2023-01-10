from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    title = models.CharField(max_length=50, default=None)
    image_url = models.ImageField(upload_to='images/', default=None)
    pub_date = models.DateTimeField(null=True)
    reporter = models.ForeignKey(User, null=True, on_delete=models.CASCADE)