from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

 
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("User Image", {"fields": ('image',)}),
        ("Your Web", {"fields": ('website',)}),
        ("Personal info in persian", {"fields": ('first_name_in_persian', 'last_name_in_persian')}),
    )

    list_display = UserAdmin.list_display + ('first_name_in_persian', )
    list_display_links = list_display
    
    
    
admin.site.register(CustomUser, CustomUserAdmin )
