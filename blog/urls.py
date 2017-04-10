from django.conf.urls import url

from . import views
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/$', views.BlogCreate.as_view(), name='create_blog'),
    url(r'^posts/(?P<pk>\d+)/$', views.view_post, name='view_blog_post'),
    url(r'^categories/(?P<pk>\d+)/$', views.view_category, name='view_blog_category'),
    url(r'^categories/$', views.view_categories, name='view_blog_categories'),
]
