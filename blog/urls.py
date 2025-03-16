from django.urls import path
from .views import home, post

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>/', post, name='post'),
]