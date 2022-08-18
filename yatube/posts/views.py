from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    title = 'Yatube'
    text = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'text': text
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Yatube'
    text = 'Здесь будет информация о проектах Yatube'
    context = {
        'title': title,
        'text': text
    }
    return render(request, template, context)
