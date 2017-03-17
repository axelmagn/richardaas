from django.shortcuts import render
from random import randint
from . import models

# Create your views here.


def dick_detail(request, pk):
    dick = models.DickPic.objects.get(pk=pk)
    context = {
        'dick_pic': dick,
    }
    return render(request, 'dick/detail.html', context)


def random_dicking(request):
    count = models.DickPic.objects.count()
    idx = randint(0, count - 1)
    dick = models.DickPic.objects.all()[idx]
    context = {
        'dick_pic': dick,
    }
    return render(request, 'dick/detail.html', context)
