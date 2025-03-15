from django.shortcuts import render
from .models import Post


def home(request):
    post = Post.objects.filter(is_published=True, is_active=True).order_by('-publish_date').last()
    return render(request, 'blog/home.html', {'post': post})
