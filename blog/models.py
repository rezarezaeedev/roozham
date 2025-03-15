from django.db import models
from datetime import date
from django.utils import timezone


class Post(models.Model):
    day_question = models.CharField(max_length=100)
    text = models.TextField(default=":( برای این روز هنوز متنی نوشته نشده است")
    secret_text = models.TextField(null=1, blank=1)
    created_at = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateField(default=date.today, unique=True)
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)


    def publish(self):
        self.is_published = True
        self.save()

    def should_be_published(self):
        return not self.is_published and self.publish_date <= timezone.now().date()
    
    def __str__(self):
        return self.day_question