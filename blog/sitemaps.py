from django.contrib.sitemaps import Sitemap
from .models import Post
from datetime import date


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        today_date = date.today()
        return Post.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return f'/post/{obj.slug}/'
