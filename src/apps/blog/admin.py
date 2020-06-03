from django.contrib import admin

from apps.blog.models import Post, Comment, Photo


@admin.register(Post)
class BlogPostModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoModelAdmin(admin.ModelAdmin):
    pass
