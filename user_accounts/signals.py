from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image
import os
from io import BytesIO
from django.core.files.base import ContentFile
from .models import CustomUser  

@receiver(pre_save, sender=CustomUser)  
def compress_image(sender, instance, **kwargs):
    if instance.image:  
        img = Image.open(instance.image)
    
        max_size = (1024, 1024)
        img.thumbnail(max_size)   

        img_format = "WEBP"  
        img_io = BytesIO()
        img.save(img_io, format=img_format, quality=80)  
        
        instance.image.save(f"{instance.image.name.split('.')[0]}.webp", 
                            ContentFile(img_io.getvalue()), save=False)
