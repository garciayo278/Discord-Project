from django.contrib import admin
from .models import (
    Guest, Venue, Event, RSVP, PhotoCategory, Photo,
    Table, SeatingAssignment, GiftRegistry, Newsletter,
    NewsletterLog, GuestMessage
)

# Register your models here.

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'plus_one_allowed', 'newsletter_subscribed', 'created']
    list_filter = ['plus_one_allowed', 'newsletter_subscribed', 'created']
    search_fields = ['first_name', 'last_name', 'email']
    ordering = ['last_name', 'first_name']


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'capacity']
    search_fields = ['name', 'city', 'address']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'event_type', 'venue', 'date_time', 'display_order']
    list_filter = ['event_type', 'venue']
    ordering = ['date_time', 'display_order']


@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ['guest', 'event', 'response', 'meal_choice', 'plus_one_attending', 'responded_at']
    list_filter = ['response', 'event', 'plus_one_attending']
    search_fields = ['guest__first_name', 'guest__last_name']
    ordering = ['-responded_at']


@admin.register(PhotoCategory)
class PhotoCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_order']
    ordering = ['display_order']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'display_order', 'created']
    list_filter = ['is_featured', 'category']
    search_fields = ['title', 'caption']
    ordering = ['display_order', '-created']


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'table_name', 'capacity', 'event', 'seats_available']
    list_filter = ['event']
    ordering = ['table_number']


@admin.register(SeatingAssignment)
class SeatingAssignmentAdmin(admin.ModelAdmin):
    list_display = ['guest', 'table', 'seat_number']
    list_filter = ['table']
    search_fields = ['guest__first_name', 'guest__last_name']


@admin.register(GiftRegistry)
class GiftRegistryAdmin(admin.ModelAdmin):
    list_display = ['name', 'registry_type', 'is_active', 'display_order']
    list_filter = ['registry_type', 'is_active']
    ordering = ['display_order']


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['subject', 'is_sent', 'sent_date', 'send_to_all', 'created']
    list_filter = ['is_sent', 'send_to_all']
    ordering = ['-created']


@admin.register(NewsletterLog)
class NewsletterLogAdmin(admin.ModelAdmin):
    list_display = ['newsletter', 'guest', 'sent_at', 'opened_at', 'clicked', 'bounced']
    list_filter = ['clicked', 'bounced']
    search_fields = ['guest__first_name', 'guest__last_name']
    ordering = ['-sent_at']


@admin.register(GuestMessage)
class GuestMessageAdmin(admin.ModelAdmin):
    list_display = ['guest', 'is_approved', 'is_public', 'created']
    list_filter = ['is_approved', 'is_public']
    search_fields = ['guest__first_name', 'guest__last_name', 'message']
    ordering = ['-created']
