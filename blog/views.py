from django.shortcuts import render, get_object_or_404
from .models import Post


def all_post(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def details(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/details.html', {'post': post})
