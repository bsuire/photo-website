from django.shortcuts import render

albums={"toronto":34,"montreal":0}
album_names=albums.keys()
picture_paths= []

def home(request):
    context = {}
    return render(request,'photos/home.html',context)

def aboutme(request):
    context = {}
    return render(request,'photos/aboutme.html',context)

def gallery(request,album_name):
    context = {'album_name':album_name}
    if (album_names.count(album_name) == 0):
        return render(request,'photos/error404.html',context)
    else:
        generatePicturePaths(album_name)
        context['pictures']=picture_paths
        return render(request,'photos/gallery.html',context)

def pageNotFound(request,album_name):
    context = {'album_name':album_name}
    return render(request,'photos/error404.html',context)


def generatePicturePaths(name):
    del picture_paths[0:len(picture_paths)] 
    for x in range(1,albums[name]+1):
        picture_paths.append('photos/'+name+'/'+name+'-'+str(x)+'.jpg')
