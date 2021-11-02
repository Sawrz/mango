from django.contrib import admin
from main.admin import MarkdownAdmin
from .models import Project


# Register your models here.
@admin.register(Project)
class ProjectAdmin(MarkdownAdmin):
    list_display = ('id',
                    'name',
                    'date_created',
                    'date_modified',
                    'show_up',
                    'slug',
                    )
    list_filter = ('show_up',
                   'date_created',
                   )
    list_editable = (
        'show_up',
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
