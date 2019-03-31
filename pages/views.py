from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from listings.models import Listing
from owners.models import Owner
from listings.choices import price_choices,bedroom_choices,state_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]

    context = {
        'listings': listings,
        'state_choices':state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }

    return render(request, 'pages/index.html',context)

def about(request):

    owners = Owner.objects.order_by('-hire_date')
    mvp_owner = Owner.objects.all().filter(is_mvp = True)

    context = {
        'owners': owners,
        'mvp_owner': mvp_owner
    }

    return render(request, 'pages/about.html',context)