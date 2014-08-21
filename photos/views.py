from django.shortcuts import render

album_sizes={"toronto":34,"montreal":0,"madagascar":0,"vosges":14}
#album_titles={"toronto":"Toronto","montreal":"Montreal"}
album_names=["toronto","montreal","madagascar", "vosges"] #album_sizes.keys() returns keys sorted alphabetically
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
        prevNext = getPreviousAndNext(album_name)
        context['pictures']=picture_paths
        context['previous']=prevNext[0]
        context['next']=prevNext[1]
        return render(request,'photos/gallery.html',context)

def pageNotFound(request,album_name):
    context = {'album_name':album_name}
    return render(request,'photos/error404.html',context)


#######################################################################################
####                    Helper functions
#######################################################################################


#######################################################################################
####    generatePicturePath: updates array picture_paths with the appropriate
####                         picture folder and name.
#######################################################################################
def generatePicturePaths(name):
    del picture_paths[0:len(picture_paths)] 
    for x in range(1,album_sizes[name]+1):
        picture_paths.append('photos/'+name+'/'+name+'-'+str(x)+'.jpg')
#######################################################################################


#######################################################################################
####    getPreviousAndNext: returns a tuple with the names of the albums preceding and
####                        following the current album (with wraparound), and aready
####                        formatted with first letter uppercases
#######################################################################################
def getPreviousAndNext(name):
    i = album_names.index(name)
    
    if i+1<len(album_names):
        next_album = album_names[i+1]
    else:
        next_album=album_names[0] #wwaparound

    if i>0:
        prev_album = album_names[i-1]
    else:
        prev_album = album_names[len(album_names)-1] #wraparound
   
    #prev_album = album_titles[prev_album]
    #next_album = album_titles[next_album]

    return (prev_album,next_album)
#######################################################################################
