from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    #var_dump = Project.objects.all().values()
    return render(request, 'portfolio/home.html', {'projects': projects})
