from django.shortcuts import render

def home(request):
    context = {}
    return render(request,'photos/home.html',context)


# Create your views here.
