from django.http import HttpResponse
from django.shortcuts import render
from .models import Nation


def index(request):
    nations = Nation.objects.filter()
    return render(request, 'index.html',
                  {'nations' : nations})

