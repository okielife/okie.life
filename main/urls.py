"""cv_okie_life_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from .views import index, humans

urlpatterns = [
    # root view
    url(r'^$', index, name='root-index'),
    # administration page
    url(r'^admin/', admin.site.urls),
    # humans.txt, robots.txt, etc.
    url(r'^humans.txt', humans, name='humans'),
    # include each app with its own urls
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^cv/', include('cv.urls', namespace='cv')),
    url(r'^consulting/', include('consulting.urls', namespace='consulting')),
    url(r'^family/', include('family.urls', namespace='family')),
    url(r'^other/', include('other.urls', namespace='other')),
]

urlpatterns += [
    url('^accounts/', include('django.contrib.auth.urls')),
]
