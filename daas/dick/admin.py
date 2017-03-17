from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.DickPic)
class DickPicAdmin(admin.ModelAdmin):
    pass
