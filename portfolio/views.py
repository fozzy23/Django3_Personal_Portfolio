from django.shortcuts import render
from django.db import models
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
