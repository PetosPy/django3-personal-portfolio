from django.shortcuts import render
from .models import Project
from .models import Tools
from datetime import datetime

# Create your views here.
def home(request):
    year = datetime.now().year

    tools = Tools.objects.all()
    projects = Project.objects.all()

    return render(request, 'portfolio/home.html', {"projects": projects, "year": year,"tools": tools})


