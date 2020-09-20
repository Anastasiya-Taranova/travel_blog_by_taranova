from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.vietnam.models import VieDays


@admin.register(VieDays)
class UserInfoAdminModel(ModelAdmin):
    pass
