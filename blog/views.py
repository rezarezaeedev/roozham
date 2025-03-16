from .models import Post, BlogSettings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model


User = get_user_model()


def home(request):
    blogsettings = BlogSettings.objects.filter(is_active=1).last()
    post = Post.objects.filter(is_published=True, is_active=True).order_by('publish_date').last()
    return render(request, 'blog/home.html', {'post': post, 'blogsettings':blogsettings}, status=200)

def post(request, slug):
    blogsettings = BlogSettings.objects.filter(is_active=1).last()
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/home.html', {'post': post, 'blogsettings':blogsettings}, status=200)

