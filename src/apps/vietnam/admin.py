from apps.vietnam.models import VieDays
from django.contrib import admin
from django.contrib.admin import ModelAdmin


@admin.register(VieDays)
class UserInfoAdminModel(ModelAdmin):
    pass
