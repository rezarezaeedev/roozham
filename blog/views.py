from .models import Post, BlogSettings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from persiantools.jdatetime import JalaliDate


User = get_user_model()


def get_persian_date(date):
    print('*'*20)
    print(date)
    persian_months = [
        'فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور',
        'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند'
    ]
    days_of_week = [
        'شنبه', 'یک‌شنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه', 'پنج‌شنبه', 'جمعه'
    ]
    print(days_of_week[date.weekday()]  )
    weekday = days_of_week[date.weekday()]
    day = date.day
    month = persian_months[date.month - 1]
    year = date.year
    print(f'{weekday}، {day} {month} {year}')
    return f'{weekday}، {day} {month} {year}'


def home(request):
    blogsettings = BlogSettings.objects.filter(is_active=1).last()
    post = Post.objects.filter(is_published=True, is_active=True).order_by('publish_date').last()
    post_publish_date = JalaliDate(post.publish_date)
    post_publish_date = get_persian_date(post_publish_date)
    return render(request, 'blog/home.html', {'post': post, 'blogsettings':blogsettings, 'publish_date':post_publish_date}, status=200)

def post(request, slug):
    blogsettings = BlogSettings.objects.filter(is_active=1).last()
    post = get_object_or_404(Post, slug=slug)
    post_publish_date = JalaliDate(post.publish_date)
    post_publish_date = get_persian_date(post_publish_date)
    return render(request, 'blog/home.html', {'post': post, 'blogsettings':blogsettings, 'publish_date':post_publish_date}, status=200)

