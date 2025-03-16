from django.shortcuts import render
from .models import Post, BlogSettings
from django.contrib.auth import get_user_model


User = get_user_model()


def home(request):
    user = User.objects.get(username='rezarezaeedev')
    blogsettings = BlogSettings.objects.filter(is_active=1).last()
    post = Post.objects.filter(is_published=True, is_active=True).order_by('-publish_date').last()
    return render(request, 'blog/home.html', {'post': post, 'user':user, 'blogsettings':blogsettings})
