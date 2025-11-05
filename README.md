# Wedding Website 💍

A beautiful, full-featured wedding website built with Django.

## Features

- 🎨 **Elegant Design** - Professional wedding-themed interface
- 📸 **Photo Carousel** - Animated homepage slideshow
- ⏰ **Countdown Timer** - Live countdown to the big day
- 📅 **Event Management** - Ceremony, reception, and more
- 💌 **RSVP System** - Guest response tracking with meal choices
- 🖼️ **Photo Gallery** - Organized photo albums with categories
- 🎁 **Gift Registry** - Links to registry sites
- 💬 **Guestbook** - Message board for well-wishes
- 🪑 **Seating Arrangements** - Table and seat assignments
- 📧 **Newsletter System** - Email campaigns with tracking
- 📊 **Analytics** - RSVP tracking and guest insights

## Technology Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Image Handling**: Pillow
- **Deployment**: Gunicorn + Nginx (production-ready)

## Setup Instructions

### Prerequisites

- Python 3.12+
- pip
- virtualenv

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/garciayo278/Discord-Project.git
   cd studybud
   ```

2. **Create virtual environment**

   ```bash
   python -m venv django_env
   ```

3. **Activate virtual environment**

   - Windows: `django_env\Scripts\activate`
   - Mac/Linux: `source django_env/bin/activate`

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**

   ```bash
   python manage.py runserver
   ```

8. **Access the site**
   - Website: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Project Structure

```
studybud/                 # Root directory
├── wedding/              # Main wedding app
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── urls.py          # URL routing
│   ├── admin.py         # Admin configuration
│   └── templates/       # HTML templates
├── wedding_site/         # Project settings
├── media/               # Uploaded images
├── manage.py            # Django CLI
└── db.sqlite3          # Database
```

## Database Models

- **Guest** - Wedding guest information
- **Event** - Wedding events (ceremony, reception, etc.)
- **RSVP** - Guest responses and meal choices
- **Venue** - Event locations
- **Photo** - Photo gallery images
- **PhotoCategory** - Photo organization
- **Table** - Seating arrangement tables
- **SeatingAssignment** - Guest table assignments
- **GiftRegistry** - Registry links
- **Newsletter** - Email campaigns
- **NewsletterLog** - Email tracking
- **GuestMessage** - Guestbook messages

## Customization

### Update Wedding Details

Edit `wedding/templates/wedding/home.html`:

- Change couple names (line 15)
- Update wedding date (line 17)
- Adjust countdown target date (line 264)

### Change Color Scheme

Edit `wedding/templates/wedding/base.html`:

- Modify CSS variables in `:root` (lines 16-23)

### Add Photos

1. Login to admin: http://127.0.0.1:8000/admin/
2. Go to Photos → Add Photo
3. Check "Is featured" for carousel display

## Production Deployment

### With Gunicorn + Nginx

1. **Install Gunicorn**

   ```bash
   pip install gunicorn
   ```

2. **Collect static files**

   ```bash
   python manage.py collectstatic
   ```

3. **Run Gunicorn**

   ```bash
   gunicorn wedding_site.wsgi:application --bind 0.0.0.0:8000
   ```

4. **Configure Nginx** (see deployment docs)

## Future Enhancements

- [ ] Guest login system
- [ ] Interactive seating chart (drag & drop)
- [ ] Photo upload by guests
- [ ] Real-time RSVP updates
- [ ] Email automation
- [ ] CSV guest import
- [ ] Analytics dashboard
- [ ] Mobile app

## License

Private project - All rights reserved

## Contact

For questions or support, contact the developer.

---

Built with ❤️ for a special day
