from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, state_choices, price_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings':listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    seller_of_the_month = Realtor.objects.all().filter(is_mvp=True)
    realtors = Realtor.objects.all()
    context = {
        'realtors':realtors,
        'seller_of_the_month':seller_of_the_month,
    }
    return render(request, 'pages/about.html', context)