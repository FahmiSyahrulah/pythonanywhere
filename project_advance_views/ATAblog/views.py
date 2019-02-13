from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone
from .form import PostForm

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blogs' : blog})

def input_post(request):
   if request.method == "POST":
       form = PostForm(request.POST)
       if form.is_valid():
           post = form.save(commit=False)
           post.tanggal = timezone.now()
           post.save()
           return redirect('blog')
   else:
       form = PostForm()
   return render(request, 'post_new.html', {'form': form})