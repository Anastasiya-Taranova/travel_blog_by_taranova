
from apps.index.models import TripInfo
from django.contrib import admin
from django.contrib.admin import ModelAdmin


@admin.register(TripInfo)
class UserInfoAdminModel(ModelAdmin):
    pass
