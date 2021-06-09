from django.shortcuts import render


def index(request):
    context = {'title': 'My Blog'}
    return render(request, 'posts/index.html', context)


def post(request):
    context = {'title': 'My Blog - Пост'}
    return render(request, 'posts/post.html', context)
