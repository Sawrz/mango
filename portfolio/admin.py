from django.contrib import admin
from main.admin import MarkdownAdmin
from .models import Project


# Register your models here.
@admin.register(Project)
class ProjectAdmin(MarkdownAdmin):
    list_display = ('id',
                    'name',
                    'category',
                    'publish_date',
                    'date_modified',
                    'date_finished',
                    'published',
                    'slug',
                    )
    list_filter = ('published',
                   'publish_date',
                   'date_finished',
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


