from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    # Display the items in page
    list_display = (
        'id','title','is_published','price','realtor', 'list_date',
    )

    list_display_links = (
        'id','title'
    )
    # filters the item 
    list_filter = (
        'realtor',
    )
    list_editable = (
        'is_published',
    )
    search_fields = (
        'title', 'description', 'address', 'city', 'state', 'zipcode', 'price',
    )
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)