from django.contrib.admin import ModelAdmin
from django.contrib import admin

from apps.vietnam.models import VieDays, Responsibility
from apps.vietnam.models import Add


@admin.register(VieDays)
class UserInfoAdminModel(ModelAdmin):
    pass
@admin.register(Add)
class UserInfoAdminModel(ModelAdmin):
    pass
@admin.register(Responsibility)
class UserInfoAdminModel(ModelAdmin):
    pass

