from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'hire_date', 'is_mvp',
    )
    list_display_links = (
        'email',
    )
    search_fields = (
        'name',
    )
    list_per_page = 25

    list_editable = (
        'name', 'is_mvp',
    )

admin.site.register(Realtor, RealtorAdmin)