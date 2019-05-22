from django.shortcuts import render
from .models import aboutus

# Create your views here.
def about(request):
    context ={
        "description": aboutus.objects.get()
    }
    return render(request,'about/about.html',context)
