from django.shortcuts import render
from .models import delayinfo

# Create your views here.

def show_delayinfo(request):
    delays = delayinfo.objects.all()
    return render(request, 'index.html', {'delays': delays})