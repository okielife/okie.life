from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='cv-index'),
    url(r'^publications/', views.publications, name='cv-publications'),
    url(r'^education/', views.education, name='cv-education'),
    url(r'^experience/', views.experience, name='cv-experience'),
    url(r'^skills/', views.skills, name='cv-skills'),
    url(r'^memberships/', views.memberships, name='cv-memberships'),
    url(r'^projects/', views.projects, name='cv-projects'),
    url(r'^html/', views.html, name='cv-html'),
    url(r'^pdf/', views.pdf, name='cv-pdf'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
