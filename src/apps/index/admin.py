from django.contrib.admin import ModelAdmin
from django.contrib import admin
from apps.index.models import TripInfo


@admin.register(TripInfo)
class UserInfoAdminModel(ModelAdmin):
    pass
