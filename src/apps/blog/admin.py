from django.contrib.admin import ModelAdmin
from django.contrib import admin
from apps.blog.models import BlogPost


@admin.register(BlogPost)
class UserInfoAdminModel(ModelAdmin):
    pass
