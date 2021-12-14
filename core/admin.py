from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.conf import settings
from .models import Profile, SocialMediaProfile, Media, Testimonial, Certificate, SoftSkill, TechnicalSkill, \
    TechnicalSubskill


# Set Title
admin.site.site_header = 'Mango Admin'

# Unregister models
if not settings.MAINTENANCE or settings.DEBUG:
    admin.site.unregister(Group)
    admin.site.unregister(User)


# Register your models here.
@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'user',
                    'job_title')


@admin.register(SocialMediaProfile)
class SocialMediaProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# Register your models here.
@admin.register(TechnicalSkill)
class TechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'score',
                    'is_active',
                    )
    list_filter = ('is_active',
                   )
    list_editable = ('is_active',
                     )
    search_fields = ('name',
                     )
    prepopulated_fields = {
        "slug": (
            "name",
        )
    }


@admin.register(TechnicalSubskill)
class TechnicalSubSkillAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'weight',
                    'score',
                    )
    list_filter = ('technical_skill',
                   'weight',
                   )
    list_editable = ('weight',
                     'score',
                     )
    search_fields = ('name',
                     )


@admin.register(SoftSkill)
class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'is_active')
    list_filter = ('is_active',
                   )
    list_editable = ('is_active',
                     )
    search_fields = ('name',
                     )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name',
                    'last_name',
                    'is_active',
                    )
    list_filter = ('is_active',
                   )
    list_editable = ('is_active',
                     )
    search_fields = ('first_name',
                     'last_name',
                     'role',
                     )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'institution',
                    'date_received',
                    'is_active')
    list_filter = ('is_active',
                   )
    list_editable = ('is_active',
                     )
    search_fields = ('title',
                     'institution',
                     'is_active',
                     )
