from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from .choices import bedroom_choices, state_choices, price_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings,
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    # listing = Listing.objects.get(pk=listing_id)
    context = {
        'listing' : listing,
    }
    return render(request, 'listings/listing.html', context)

def search(request):

    query_set = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set = query_set.filter(description__icontains=keywords)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_set = query_set.filter(city__iexact=city)
    
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_set = query_set.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_set = query_set.filter(bedrooms__iexact=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_set = query_set.filter(price__lte=price)


        
    context = {
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices,
        'price_choices':price_choices,
        'listings':query_set,
        'values':request.GET
    }



    return render(request, 'listings/search.html', context)