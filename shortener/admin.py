from django.contrib import admin
from .models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'original_url', 'created_by', 'click_count', 'created_at' )
    readonly_fields = ('short_code', 'click_count', 'created_at')


