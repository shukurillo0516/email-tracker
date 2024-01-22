from django.contrib import admin
from .models import *


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "user", "url"]
    list_display_links = ["id", "name", "user"]
    raw_id_fields = ["user"]
    readonly_fields = ["url"]


@admin.register(LinkRecord)
class LinkRecordAdmin(admin.ModelAdmin):
    list_display = ["id", "link", "created_at"]
    list_display_links = ["id", "link", "created_at"]
