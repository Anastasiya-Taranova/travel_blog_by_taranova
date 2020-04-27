from django.contrib.admin import ModelAdmin
from django.contrib import admin
from apps.vietnam.models import VieDays


@admin.register(VieDays)
class UserInfoAdminModel(ModelAdmin):
    pass
