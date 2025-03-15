from celery import shared_task
from django.utils import timezone
from .models import BlogPost

@shared_task
def publish_scheduled_posts():
    """پست‌هایی که باید منتشر شوند را پیدا کرده و منتشر می‌کند"""
    today = timezone.now().date()
    posts = BlogPost.objects.filter(is_active=False, publish_date=today, is_published=False)
    
    for post in posts:
        post.is_published = True
        post.save()
