from django.contrib import admin

from apps.blog.models import Comment
from apps.blog.models import Photo
from apps.blog.models import Post


@admin.register(Post)
class BlogPostModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoModelAdmin(admin.ModelAdmin):
    pass
