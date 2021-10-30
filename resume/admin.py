from django.contrib import admin
from .models import Profile, Testimonial, Certificate, SoftSkill, TechnicalSkill


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
    list_editable = ('score',
                     'is_active',
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


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'main_profile',
                    'job_title')


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
