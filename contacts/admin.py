from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'message',
    )
    list_display_links = (
        'username',
    )
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)