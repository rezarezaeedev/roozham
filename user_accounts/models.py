from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name_in_persian = models.CharField(max_length=50, null=1, blank=1)
    last_name_in_persian = models.CharField(max_length=50, null=1, blank=1)
    image = models.ImageField(upload_to='user_profile_images/', blank=True, null=True)
    website = models.URLField(max_length=100,  blank=True, null=True)

    def get_full_name_in_persian(self):
        return f'{self.first_name_in_persian} {self.last_name_in_persian}'