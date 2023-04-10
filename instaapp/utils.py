from django.utils import timezone
from datetime import timedelta
from .models import Profile

from django import template
register = template.Library()

@register.filter(name='get_time_since_posted')
def get_time_since_posted(posted_time):
    now = timezone.now()
    diff = now - posted_time

    if diff < timedelta(minutes=1):
        return 'Just now'
    elif diff < timedelta(hours=1):
        minutes = int(diff.total_seconds() // 60)
        return f'{minutes} minute{"s" if minutes > 1 else ""} ago'
    elif diff < timedelta(days=1):
        hours = int(diff.total_seconds() // 3600)
        return f'{hours} hour{"s" if hours > 1 else ""} ago'
    elif diff < timedelta(weeks=1):
        days = int(diff.total_seconds() // 86400)
        return f'{days} day{"s" if days > 1 else ""} ago'
    else:
        weeks = int(diff.total_seconds() // 604800)
        return f'{weeks} week{"s" if weeks > 1 else ""} ago'

@register.filter(name='get_profile_image_url')
def get_profile_image_url(userid):
    profile = Profile.objects.get(user=userid)
    return profile.profile_pic.url if profile and profile.profile_pic else ''