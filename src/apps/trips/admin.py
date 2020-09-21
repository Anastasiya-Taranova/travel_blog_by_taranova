from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.trips.models import Photo, Content, PointsMap, Countries


@admin.register(Countries)
class UserInfoAdminModel(ModelAdmin):
    pass

@admin.register(PointsMap)
class UserInfoAdminModel(ModelAdmin):
    pass

@admin.register(Content)
class UserInfoAdminModel(ModelAdmin):
    pass

@admin.register(Photo)
class UserInfoAdminModel(ModelAdmin):
    pass
