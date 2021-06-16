from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Category
from .forms import CommentForm

from django.utils import timezone

# Create your views here.

def home(request):
    blogs = Blog.objects.all() #쿼리셋
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, id):
    details = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html',{'details': details})

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html',{'blogs': blogs})

def about_me(request):
    return render(request, 'about_me.html')

def delete(request, id):
    delete_blog = Blog.objects.get (id=id)
    delete_blog.delete()
    return redirect('index')

def new(request):
    return render (request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.image = request.FILES['image']
    new_blog.save()
    return redirect('detail',new_blog.id)

def edit(request,id):
    edit_blog = Blog.objects.get(id=id)
    return render (request,'edit.html',{'blog': edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('detail',update_blog.id)

def add_comment_to_post(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=blog
            comment.save()
            return redirect('detail', blog_id)
        else:
            form=CommentForm()
        return render(request, 'add_comment_to_post.html', {'form':form})



