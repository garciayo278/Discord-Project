from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Event, Photo, GiftRegistry, GuestMessage, RSVP

# Create your views here.

def home(request):
    """Homepage with photo carousel and welcome message"""
    featured_photos = Photo.objects.filter(is_featured=True)[:5]
    upcoming_events = Event.objects.filter(date_time__gte=timezone.now())[:3]
    
    context = {
        'featured_photos': featured_photos,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'wedding/home.html', context)


def our_story(request):
    """About us / our story page"""
    context = {}
    return render(request, 'wedding/our_story.html', context)


def events(request):
    """List all wedding events with details"""
    all_events = Event.objects.all()
    context = {'events': all_events}
    return render(request, 'wedding/events.html', context)


def gallery(request):
    """Photo gallery with categories"""
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'wedding/gallery.html', context)


def rsvp(request):
    """RSVP form for guests"""
    if request.method == 'POST':
        # Handle RSVP submission (we'll build this fully later)
        messages.success(request, 'Thank you for your RSVP!')
        return redirect('wedding:home')
    
    events_list = Event.objects.all()
    context = {'events': events_list}
    return render(request, 'wedding/rsvp.html', context)


def registry(request):
    """Gift registry links"""
    registries = GiftRegistry.objects.filter(is_active=True)
    context = {'registries': registries}
    return render(request, 'wedding/registry.html', context)


def guestbook(request):
    """Guestbook for messages"""
    if request.method == 'POST':
        # Handle message submission (we'll build this fully later)
        messages.success(request, 'Thank you for your message!')
        return redirect('wedding:guestbook')
    
    approved_messages = GuestMessage.objects.filter(is_approved=True, is_public=True)
    context = {'messages': approved_messages}
    return render(request, 'wedding/guestbook.html', context)
