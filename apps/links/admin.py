from django.contrib import admin
from .models import *


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "user", "url"]
    list_display_links = ["id", "name", "user"]
    readonly_fields = ["url", "created_at", "updated_at"]
    raw_id_fields = ["user"]


@admin.register(LinkRecord)
class LinkRecordAdmin(admin.ModelAdmin):
    list_display = ["id", "link", "created_at"]
    list_display_links = ["id", "link", "created_at"]
    readonly_fields = ["created_at", "updated_at"]
