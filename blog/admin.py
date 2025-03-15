from django.contrib import admin
from .models import Post


# class ReviewInline(admin.TabularInline):  # یا StackedInline برای نمایش عمودی
#     model = Review
#     extra = 1  # تعداد فیلدهای خالی جدید


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['day_question', 'show_secret_text', 'publish_date', 'slug', 'is_published', 'is_active', 'created_at']
    list_editable = ['is_published', 'is_active']
    list_display_links = ['day_question', 'show_secret_text', 'publish_date', 'slug', 'created_at']
    list_filter = ['publish_date', 'is_published', 'is_active', 'created_at']
    ordering = ['-publish_date', ]
    search_fields = ['day_question', 'secret_text', 'slug',  'publish_date', ]
    # list_max_show_all = 100
    # list_per_page = 20
    
    fieldsets = (
        ("امروز پاسخ دهید",{'fields':('day_question', 'text', 'secret_text'),}),
        ("روزنوشت خود را پیکربندی کنید",{'fields':('slug', 'publish_date'),}),
        ('وضعیت انتشار را تعیین کنید',{'fields':('is_published', 'is_active' ),}),
    )

    # inlines = [ReviewInline]

    @admin.display(description='Has secret text')
    def show_secret_text(self, obj):
        print(obj.publish_date)
        return "Yes" if obj.secret_text else 'No'
