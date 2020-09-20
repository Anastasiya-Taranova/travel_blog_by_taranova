from django.contrib import admin

from apps.photos.models import Photos


@admin.register(Photos)
class BlogPostModelAdmin(admin.ModelAdmin):
    pass
