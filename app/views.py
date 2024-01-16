from django.shortcuts import render

# Create your views here.

def userfilters(request):
    d={'data':'HAI HOw Are You'}
    return render(request,'userfilters.html',d)