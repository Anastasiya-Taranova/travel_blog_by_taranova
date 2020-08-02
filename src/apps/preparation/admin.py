from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.preparation.models import Skyscanner


@admin.register(Skyscanner)
class UserInfoAdminModel(ModelAdmin):
    pass
