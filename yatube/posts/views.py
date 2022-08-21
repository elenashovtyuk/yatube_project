from django.shortcuts import render
from .models import Post

# Create your views here.
from django.http import HttpResponse


def index(request):

    #template = 'posts/index.html'
    #title = 'Yatube'
    #text = 'Это главная страница проекта Yatube'
    #context = {
        #'title': title,
        #'text': text
    #}
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,

    }
    return render(request, 'posts/group_list.html', context)
    #template = 'posts/group_list.html'
    #title = 'Yatube'
    #text = 'Здесь будет информация о проектах Yatube'
    #context = {
    #    'title': title,
    #   'text': text
    # }
    #return render(request, template, context)
