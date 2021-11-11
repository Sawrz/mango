from django.contrib import admin
from main.admin import MarkdownAdmin
from .models import DataAnalysis, SoftwareProject


# Register your models here.
@admin.register(DataAnalysis)
class DataAnlysisAdmin(MarkdownAdmin):
    list_display = ('id',
                    'name',
                    'date_created',
                    'date_modified',
                    'published',
                    'slug',
                    )
    list_filter = ('published',
                   'date_created',
                   )
    list_editable = (
        'published',
    )
    search_fields = (
        'name',
        'slug',
        'body',
    )

    prepopulated_fields = {
        "slug": (
            "name",
        )
    }


@admin.register(SoftwareProject)
class SoftwareProjectAdmin(MarkdownAdmin):
    list_display = ('id',
                    'name',
                    'date_created',
                    'date_modified',
                    'published',
                    'slug',
                    )
    list_filter = ('published',
                   'date_created',
                   )
    list_editable = (
        'published',
    )
    search_fields = (
        'name',
        'slug',
        'body',
    )

    prepopulated_fields = {
        "slug": (
            "name",
        )
    }
