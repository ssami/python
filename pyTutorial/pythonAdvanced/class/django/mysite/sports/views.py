# Create your views here.

from django.shortcuts import render
from sports.models import Sports

def home(request):
    context = {
               'sports' : Sports.objects.all()
        }
    return render(request, 
                  'sports/index.html', 
                  context)
    
    
    