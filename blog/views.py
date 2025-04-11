from .models import Post, BlogSettings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from persiantools.jdatetime import JalaliDate
from datetime import date

User = get_user_model()


def get_persian_date(mydate):
    persian_months = [
        'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور',
        'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند'
    ]
    days_of_week = [
        'شنبه', 'یک‌شنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنج‌شنبه', 'جمعه'
    ]
    weekday = days_of_week[mydate.weekday()]
    day = mydate.day
    month = persian_months[mydate.month - 1]
    year = mydate.year
    return f'{weekday}، {day} {month} {year}'

def get_before_after_post_slug(mydate):
    before_post = Post.objects.filter(publish_date__lt=mydate, is_active=True, is_published=True).order_by('publish_date').last()
    after_post = Post.objects.filter(publish_date__gt=mydate, is_active=True, is_published=True).order_by('publish_date').first()
    before_slug = before_post.slug if before_post else ''
    after_slug = after_post.slug if after_post else ''
    return before_slug ,after_slug

def home(request):
    today_date = date.today()
    blogsettings = BlogSettings.objects.filter(is_active=1).last()
    post = Post.objects.filter(publish_date__lte=today_date, is_published=True, is_active=True).order_by('publish_date').last()
    if not post:
        return render(request, 'blog/welcome.html', status=200)
    post_publish_date = JalaliDate(post.publish_date)
    post_publish_date = get_persian_date(post_publish_date)
    before_post_slug, after_post_slug = get_before_after_post_slug(post.publish_date)
    return render(request, 'blog/home.html', {'post': post, 'blogsettings':blogsettings, 'publish_date':post_publish_date, 'before_post_slug':before_post_slug, 'after_post_slug':after_post_slug}, status=200)

def post(request, slug):
    blogsettings = BlogSettings.objects.filter(is_active=1).last()
    post = get_object_or_404(Post, slug=slug, is_active=True, is_published=True)
    post_publish_date = JalaliDate(post.publish_date)
    post_publish_date = get_persian_date(post_publish_date)
    before_post_slug, after_post_slug = get_before_after_post_slug(post.publish_date)
    return render(request, 'blog/home.html', {'post': post, 'blogsettings':blogsettings, 'publish_date':post_publish_date, 'before_post_slug':before_post_slug, 'after_post_slug':after_post_slug}, status=200)

