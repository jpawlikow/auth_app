from django.contrib import admin
from .models import UserProfile, Site

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass
