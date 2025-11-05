from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

# Create your models here.

class Guest(models.Model):
    """
    Guest model - stores wedding guest information
    Replaces the concept of User from StudyBud
    """
    # Basic Info
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone = models.CharField(max_length=20, blank=True)
    
    # Plus One Info
    plus_one_allowed = models.BooleanField(default=False)
    plus_one_name = models.CharField(max_length=200, blank=True)
    
    # Preferences
    dietary_restrictions = models.TextField(blank=True)
    special_notes = models.TextField(blank=True)
    
    # Newsletter
    newsletter_subscribed = models.BooleanField(default=True)
    
    # Metadata
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Venue(models.Model):
    """
    Venue model - locations for wedding events
    """
    name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    capacity = models.IntegerField()
    description = models.TextField(blank=True)
    map_url = models.URLField(blank=True, help_text="Google Maps URL")
    website = models.URLField(blank=True)
    
    # Contact
    contact_name = models.CharField(max_length=200, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_email = models.EmailField(blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Event(models.Model):
    """
    Event model - different wedding events (ceremony, reception, etc.)
    Replaces the Room concept from StudyBud
    """
    EVENT_TYPES = [
        ('CEREMONY', 'Ceremony'),
        ('RECEPTION', 'Reception'),
        ('REHEARSAL', 'Rehearsal Dinner'),
        ('BRUNCH', 'Day-After Brunch'),
        ('WELCOME', 'Welcome Party'),
        ('OTHER', 'Other'),
    ]
    
    name = models.CharField(max_length=200)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    description = models.TextField()
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, related_name='events')
    
    # Date/Time
    date_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    
    # Details
    dress_code = models.CharField(max_length=100, blank=True)
    special_instructions = models.TextField(blank=True)
    
    # Display order on site
    display_order = models.IntegerField(default=0)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['date_time', 'display_order']
    
    def __str__(self):
        return f"{self.name} - {self.get_event_type_display()}"


class RSVP(models.Model):
    """
    RSVP model - tracks guest responses to events
    Replaces the Message concept from StudyBud
    """
    RESPONSE_CHOICES = [
        ('YES', 'Attending'),
        ('NO', 'Not Attending'),
        ('MAYBE', 'Maybe'),
        ('PENDING', 'Pending'),
    ]
    
    MEAL_CHOICES = [
        ('CHICKEN', 'Chicken'),
        ('BEEF', 'Beef'),
        ('FISH', 'Fish'),
        ('VEGETARIAN', 'Vegetarian'),
        ('VEGAN', 'Vegan'),
        ('KIDS', 'Kids Meal'),
    ]
    
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='rsvps')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rsvps')
    
    # Response
    response = models.CharField(max_length=10, choices=RESPONSE_CHOICES, default='PENDING')
    responded_at = models.DateTimeField(null=True, blank=True)
    
    # Plus One
    plus_one_attending = models.BooleanField(default=False)
    
    # Meal Choices
    meal_choice = models.CharField(max_length=20, choices=MEAL_CHOICES, blank=True)
    plus_one_meal_choice = models.CharField(max_length=20, choices=MEAL_CHOICES, blank=True)
    
    # Additional Info
    notes = models.TextField(blank=True)
    song_request = models.CharField(max_length=200, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['guest', 'event']
        ordering = ['-responded_at']
    
    def __str__(self):
        return f"{self.guest.full_name} - {self.event.name}: {self.get_response_display()}"


class PhotoCategory(models.Model):
    """
    Photo categories for organizing gallery
    Replaces Topic concept from StudyBud
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    display_order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['display_order', 'name']
        verbose_name_plural = "Photo Categories"
    
    def __str__(self):
        return self.name


class Photo(models.Model):
    """
    Photo model - wedding photos for galleries and carousel
    """
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='wedding_photos/%Y/%m/')
    category = models.ForeignKey(PhotoCategory, on_delete=models.SET_NULL, null=True, related_name='photos')
    caption = models.TextField(blank=True)
    
    # Display settings
    is_featured = models.BooleanField(default=False, help_text="Show in homepage carousel")
    display_order = models.IntegerField(default=0)
    
    # Guest uploads
    uploaded_by = models.ForeignKey(Guest, on_delete=models.SET_NULL, null=True, blank=True, related_name='uploaded_photos')
    
    # Metadata
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order', '-created']
    
    def __str__(self):
        return self.title


class Table(models.Model):
    """
    Table model - for seating arrangements
    """
    table_number = models.IntegerField(unique=True)
    table_name = models.CharField(max_length=100, blank=True, help_text="e.g., 'College Friends', 'Family'")
    capacity = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tables')
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['table_number']
    
    def __str__(self):
        return f"Table {self.table_number}" + (f" - {self.table_name}" if self.table_name else "")
    
    @property
    def seats_available(self):
        assigned = self.seating_assignments.count()
        return self.capacity - assigned


class SeatingAssignment(models.Model):
    """
    Seating assignment - which guest sits at which table
    """
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='seating_assignments')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='seating_assignments')
    seat_number = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['guest', 'table']
    
    def __str__(self):
        return f"{self.guest.full_name} at {self.table}"


class GiftRegistry(models.Model):
    """
    Gift registry links
    """
    REGISTRY_TYPES = [
        ('STORE', 'Store Registry'),
        ('CASH', 'Cash Fund'),
        ('CHARITY', 'Charity Donation'),
        ('HONEYMOON', 'Honeymoon Fund'),
    ]
    
    name = models.CharField(max_length=200)
    registry_type = models.CharField(max_length=20, choices=REGISTRY_TYPES)
    url = models.URLField()
    description = models.TextField(blank=True)
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order', 'name']
        verbose_name_plural = "Gift Registries"
    
    def __str__(self):
        return f"{self.name} ({self.get_registry_type_display()})"


class Newsletter(models.Model):
    """
    Newsletter model - for email campaigns to guests
    """
    subject = models.CharField(max_length=200)
    content_html = models.TextField(help_text="Rich HTML content")
    content_plain = models.TextField(help_text="Plain text fallback")
    
    # Sending
    sent_date = models.DateTimeField(null=True, blank=True)
    is_sent = models.BooleanField(default=False)
    
    # Recipients (specific guests or all)
    recipients = models.ManyToManyField(Guest, related_name='newsletters', blank=True)
    send_to_all = models.BooleanField(default=False, help_text="Send to all subscribed guests")
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return f"{self.subject} - {'Sent' if self.is_sent else 'Draft'}"


class NewsletterLog(models.Model):
    """
    Newsletter log - tracking email opens, clicks (data engineering!)
    """
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='logs')
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='newsletter_logs')
    
    # Tracking
    sent_at = models.DateTimeField(auto_now_add=True)
    opened_at = models.DateTimeField(null=True, blank=True)
    clicked = models.BooleanField(default=False)
    clicked_at = models.DateTimeField(null=True, blank=True)
    
    # Error tracking
    bounced = models.BooleanField(default=False)
    error_message = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-sent_at']
        unique_together = ['newsletter', 'guest']
    
    def __str__(self):
        return f"{self.newsletter.subject} → {self.guest.full_name}"


class GuestMessage(models.Model):
    """
    Guest messages - like a guestbook
    """
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    is_approved = models.BooleanField(default=False, help_text="Moderate before showing publicly")
    is_public = models.BooleanField(default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return f"Message from {self.guest.full_name}"
