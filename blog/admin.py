from django.contrib import admin
from .models import Post, Category, SubCategory, Tag


# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name')

    search_fields = (
        'name',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name')

    search_fields = (
        'name',
    )


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'category')

    list_filter = ('category',
                   )

    search_fields = (
        'name',
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'subtitle',
                    'publish_date',
                    'published',
                    'slug',
                    )
    list_filter = ('published',
                   'publish_date',
                   )
    list_editable = (
        'publish_date',
        'published',
    )
    search_fields = (
        'title',
        'subtitle',
        'slug',
        'body',
    )

    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }

    date_hierarchy = "publish_date"
