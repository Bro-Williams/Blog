from django.shortcuts import render

from posts.models import Post


def index(request):
    context = {'title': 'My Blog', 'posts': Post.objects.all()}
    return render(request, 'posts/index.html', context)


def post(request):
    context = {'title': 'My Blog - Пост'}
    return render(request, 'posts/post.html', context)
