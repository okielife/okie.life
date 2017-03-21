from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mycards/$', views.MyCardInstancesListView.as_view(), name='my-cards'),
    url(r'^cardinstances/(?P<pk>[-\w]+)', views.CardInstanceDetailView.as_view(), name='cardinstance-detail'),
    url(r'^cards/$', views.AllCardsView.as_view(), name='all-cards'),
    url(r'^cards/(?P<pk>\d+)$', views.CardDetailView.as_view(), name='card-detail'),
    url(r'^cards/create/', views.create_card, name='create-card'),
    url(r'^cards/ajax_create_card/', views.ajax_create_card, name='ajax-create-card'),
    url(r'^cards/character-available/', views.ajax_char_available, name='character-available'),
]