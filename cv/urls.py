from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

app_name = 'cv'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^publications/', views.publications, name='publications'),
    url(r'^education/', views.education, name='education'),
    url(r'^experience/', views.experience, name='experience'),
    url(r'^skills/', views.skills, name='skills'),
    url(r'^memberships/', views.memberships, name='memberships'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^html/', views.html, name='html'),
    url(r'^pdf/', views.pdf, name='pdf'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
