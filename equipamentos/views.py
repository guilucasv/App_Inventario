from django.shortcuts import render
from models import Desktop


def Desktop(request):
    desktops = Desktop.objects.all()
    return render(request, 'desktop.html', {'desktops':desktops})

# Create your views here.
