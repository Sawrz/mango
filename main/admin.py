from django.contrib import admin
from .models import Profile, SocialMediaProfile, Media


# Register your models here.
@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(SocialMediaProfile)
class SocialMediaProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
