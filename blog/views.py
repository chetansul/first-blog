

# Create your views here.
from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    posts=Post.objects.all()
    return render(request,'blog/index.html',{'posts':posts})

def demo(request):
    return render(request,'blog/demo.html')

def add(request):

    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            me = User.objects.get(username="request.POST.get('author')")
            post = Post()
            post.author=me
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post. published_date=request.POST.get('date')
            post.save()

            return render(request, 'blog/demo.html')
    else:
        posts = Post.objects.all()
        return render(request, 'blog/index.html', {'posts': posts})

