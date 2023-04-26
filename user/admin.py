from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import UserAccount

# Register your models here.
# Unregister the provided model admin
# admin.site.unregister(User)

@admin.register(UserAccount)
class CustomAdmin(UserAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        if not is_superuser:
            disabled_fields |= {
                "username",
                "is_superuser",
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form

    list_display = (
        "username",
        "email",
        "created_at",
        "updated_at",
    )
    list_filter = ('is_active',)
    ordering = ("updated_at",)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "is_active",
                    "is_admin",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    filter_horizontal = ()
    fieldsets = ()
    readonly_fields = ["created_at", "last_login"]
