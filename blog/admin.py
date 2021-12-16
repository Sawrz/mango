from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, SubCategory, Tag


# Register your models here.
# @admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name')

    search_fields = (
        'name',
    )


# @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name')

    search_fields = (
        'name',
    )


# @admin.register(SubCategory)
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
    list_display = ('__str__',
                    'publish_date',
                    'get_slug',
                    'published',
                    )
    list_filter = ('published',
                   'publish_date',
                   )
    list_editable = (
        'publish_date',
    )
    search_fields = (
        'title',
        'subtitle',
        'slug',
        'body',
    )

    fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty',),
            'fields': ('title', 'subtitle', 'body', 'featured_image',)
        }),
        ('Status & Visibility', {
            'classes': ('collapse', 'extrapretty',),
            'fields': ('publish_date', 'visibility', 'author',)
        }),
        ('Presentation & SEO', {
            'classes': ('collapse', 'extrapretty',),
            'fields': ('description', 'meta_description', 'thumbnail',)
        }),
        ('Content Organization', {
            'classes': ('collapse', 'extrapretty',),
            'fields': ('category', 'tags',)
        }),
    )

    date_hierarchy = "publish_date"

    def get_slug(self, obj):
        url = reverse(f'blog:post_preview', kwargs={'slug': obj.slug})

        return format_html(f'<a href="{url}">{obj.slug}</a>')

    get_slug.short_description = 'slug'

    def save_model(self, request, obj, form, change):
        if obj.author_id is None:
            obj.author_id = request.user.id

        super(PostAdmin, self).save_model(request, obj, form, change)
