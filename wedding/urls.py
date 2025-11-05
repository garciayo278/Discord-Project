from django.urls import path
from . import views

app_name = 'wedding'

urlpatterns = [
    path('', views.home, name='home'),
    path('our-story/', views.our_story, name='our-story'),
    path('events/', views.events, name='events'),
    path('gallery/', views.gallery, name='gallery'),
    path('rsvp/', views.rsvp, name='rsvp'),
    path('registry/', views.registry, name='registry'),
    path('guestbook/', views.guestbook, name='guestbook'),
]
