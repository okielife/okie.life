from datetime import datetime

from django.forms import modelform_factory
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .forms import BlogForm
from .models import Category, Blog


def index(request):
    return render(request, 'blog/index.html', context={
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:25]  # TODO: Paginate instead of hard limit
    })


class BlogView(DetailView):
    model = Blog
    template_name = 'blog/view_post.html'


class BlogCreate(CreateView):
    model = Blog
    fields = ['title', 'body', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.created_on = datetime.now()
        return super(BlogCreate, self).form_valid(form)

    def get_form_class(self):
        return modelform_factory(self.model, form=BlogForm, fields=self.fields)


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/view_category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['posts'] = Blog.objects.filter(category=self.object.pk)
        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'blog/view_categories.html'
    paginate_by = 10
    context_object_name = 'categories'
