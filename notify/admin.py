from django.contrib import admin
from notify.models import *

class DefaultAdmin(admin.ModelAdmin):
    ordering = ("-updated_at",)

@admin.register(UserNotification)
class ClaimAdmin(DefaultAdmin):
    list_display = (
        "user",
        "category",
        "platform",
        "trigger",
    )
    search_fields = ("user__username", "user__email", "category", "platform", "trigger")
    list_filter = ("category", "platform", "trigger")
    date_hierarchy = "created_at"

# Register your models here.

