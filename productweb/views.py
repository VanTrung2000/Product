from django.shortcuts import render
from django.http import HttpResponse
from productweb.models import Products


def home(request):
    Data = {'Product': Products.objects.all()}
    return render(request,'pages/list.html', Data)
