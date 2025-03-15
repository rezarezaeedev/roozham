from celery import shared_task
from django.utils import timezone
from .models import Post

@shared_task
def publish_scheduled_posts():
    today = timezone.now().date()
    post = Post.objects.filter(is_active=True, publish_date=today, is_published=False)
    if post.exists():
        post=post.last()
        post.publish()
