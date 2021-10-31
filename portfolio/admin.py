from django.contrib import admin
from main.admin import MarkdownAdmin
from .models import Portfolio


# Register your models here.
@admin.register(Portfolio)
class PortfolioAdmin(MarkdownAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)
