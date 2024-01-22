from django.contrib import admin
from .models import *


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "url"]
    list_display_user = ["id"]
    raw_id_fields = ["user"]
    readonly_fields = ["url"]
