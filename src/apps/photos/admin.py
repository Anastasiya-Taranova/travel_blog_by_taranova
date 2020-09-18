from apps.photos.models import Photos
from django.contrib import admin


@admin.register(Photos)
class BlogPostModelAdmin(admin.ModelAdmin):
    pass
