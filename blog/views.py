from django.shortcuts import render, get_object_or_404
from .models import Category, Blog


def index(request):
    return render(request, 'blog/index.html', context={
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })


def view_post(request, pk):
    return render(request, 'blog/view_post.html', context={
        'post': get_object_or_404(Blog, pk=pk)
    })


def view_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'blog/view_category.html', context={
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })


def view_categories(request):
    categories = Category.objects.all()
    return render(request, 'blog/view_categories.html', context={
        'categories': categories
    })
