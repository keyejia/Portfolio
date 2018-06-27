from django.shortcuts import render
from .models import Project

def home(request):
	Projects = Project.objects
	return render(request, 'Projects/home.html', {'Projects':Projects})
# Create your views here.
