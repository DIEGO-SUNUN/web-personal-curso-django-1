from django.shortcuts import render

# Create your views here.
from .models import Project


def portfolio(request):
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects':projects})