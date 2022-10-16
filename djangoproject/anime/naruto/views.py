from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Newapp

def index(request):
    mymembers =Newapp.objects.all().values()
    template=loader.get_template('to-do list.html')
  
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))
# Create your views here.

