"""Pictionary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url

from pictionary.views import home, player, audience, up_vote, down_vote, get_word

app_name = 'pictionary'

urlpatterns = [
    url(r'^player/', player, name='player'),
    url(r'^audience/', audience, name='audience'),
    url(r'^up_vote/', up_vote, name='up_vote'),
    url(r'^down_vote/', down_vote, name='down_vote'),
    url(r'^get_word/', get_word, name='get_word'),
    url(r'^', home, name='index'),
]
