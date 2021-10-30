from django.contrib import admin
from .models import Profile, Testimonial, Certificate, SoftSkill, TechnicalSkill


# Register your models here.
@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'main_profile')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'is_active')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'institution')


@admin.register(SoftSkill)
class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')


@admin.register(TechnicalSkill)
class TechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score', 'is_active')
