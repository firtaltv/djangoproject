from django.contrib import admin
from .models import Snippets


@admin.register(Snippets)
class SnippetsAdmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'code', 'language', 'style', 'lineos',)
