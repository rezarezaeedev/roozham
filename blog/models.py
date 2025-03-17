from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogSettings(models.Model):
    tab_bar_title = models.CharField(max_length=100)
    page_title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    is_active = models.BooleanField(default=True)


class Post(models.Model):
    day_question = models.CharField(max_length=300)
    text = models.TextField(default=":( برای این روز هنوز متنی نوشته نشده است")
    secret_text = models.TextField(null=1, blank=1)
    created_at = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateField(default=date.today, unique=True)
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)
    keywords = models.TextField(null=1, blank=1)


    def publish(self):
        self.is_published = True
        self.save()

    def should_be_published(self):
        return not self.is_published and self.publish_date <= timezone.now().date()
    
    @property
    def get_keywords(self):
        keywords = self.keywords
        keywords = keywords.replace('،', ',')
        keywords = keywords.split(',')
        keywords = list(map(lambda x:x.strip(), keywords))
        return keywords

    def __str__(self):
        return self.day_question
    