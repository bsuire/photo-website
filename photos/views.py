from django.shortcuts import render

existing_albums=["toronto","madagascar"]

def home(request):
    context = {}
    return render(request,'photos/home.html',context)

def aboutme(request):
    context = {}
    return render(request,'photos/aboutme.html',context)

def gallery(request,album_name):
    context = {'album_name':album_name}
    if (existing_albums.count(album_name) == 0):
        return render(request,'photos/error404.html',context)
    else:
        return render(request,'photos/'+album_name+'.html',context)

def pageNotFound(request,album_name):
    context = {'album_name':album_name}
    return render(request,'photos/error404.html',context)
