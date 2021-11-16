from django.contrib import admin
from apps.prestashop.models import PrestashopSynchronizer as PrestaSync


class PrestashopSynchronizerAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "__str__",
        "resources_type",
        "entity_id",
        "status",
    )
    list_filter = ("resources_type", "status")


admin.site.register(PrestaSync, PrestashopSynchronizerAdmin)
