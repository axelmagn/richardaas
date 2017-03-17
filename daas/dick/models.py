import os

from django.db import models
from django.conf import settings

# Create your models here.

# DICK_PATH = os.path.join(settings.MEDIA_ROOT, "dicks")


class DickPic(models.Model):
    pic = models.ImageField(upload_to="dicks")
