from django.db import models
from datetime import date
from django.utils import timezone


class BlogPost(models.Model):
    day_question = models.CharField(max_length=100)
    text = models.TextField()
    publish_date = models.DateField(default=date.today)

    is_published = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=False)

    def should_be_published(self):
        return not self.is_published and self.publish_date <= timezone.now().date()
    
    def __str__(self):
        return self.day_question