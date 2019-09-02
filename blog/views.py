from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from time import timezone


def get_index(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'index.html',{"posts":posts})

    
def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request, 'post_new.html', {'form': form})

# def post_new(request):
#     form=PostForm()
#     return render(request,'post_new.html')
#     if forms.is_valid():
#         post = form.save(commit=False)
#         post.author = request.user
#         post.published_date = timezone.now()
#         post.save()

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})