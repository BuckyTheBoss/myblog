from django.shortcuts import render
from .forms import PostModelForm
from .models import Post

# Create your views here.

def new_post(request):
    form = PostModelForm()
    if request.method == "POST":
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.likes = 5
            post.save()
    return render(request, 'new_post.html', {'form': form})


def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostModelForm(instance=post)

    if request.method == "POST":
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
    return render(request, 'new_post.html', {'form': form})


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return render(request, 'new_post.html')

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post.html', {'post':post})