from django.shortcuts import render ,redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def postList(request):
    all = Post.objects.all()
    return render(request,'posts.html',{'data':all})

def postDetails(request,id):
    post =Post.objects.get(id=id)
    return render(request,'singel.html',{'onePost':post})


def createPost(request):
    '''
    wenn die Daten mit Post Methond geschickt werden (Wenn User auf submite taste drückt) ,
    dann gib mir PostForm und speischer es ,anderfalls gib mir ein leerer PostForm (noramle Öffnung der Seite)
    '''
    if request.method =='POST':
        form = PostForm (request.POST,request.FILES)
        print('in Post')
        if form.is_valid():
            " don't save the data in database now , not yet!!"
            newForm=form.save(commit=False) 
            'take the username of the user '
            newForm.author=request.user
            'now you can save'
            newForm.save()
    else:
        form = PostForm
        print('in Get')
    return render(request,'createPost.html',{'form':form})


def editPost(request,id):
    post =Post.objects.get(id=id)
    if request.method =='POST':
        form = PostForm (request.POST,request.FILES,instance=post)
        print('in Post')
        if form.is_valid():
            " don't save the data in database now , not yet!!"
            newForm=form.save(commit=False) 
            'take the username of the user '
            newForm.author=request.user
            'now you can save'
            newForm.save()
    else:
        'nimm die vorhandenen Daten als Default ,damit wir sie bearbeiten können'
        form = PostForm(instance=post) 
        print('in Get')
    return render(request,'editPost.html',{'form':form})


def deletePost(request,id):
    post =Post.objects.get(id=id)
    post.delete()
    'to redirect the user to a Page , we have to import redirect!!!!!!!!'
    return redirect ('/blog')