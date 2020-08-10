from django import forms  

from .models import Listings,Bid


class ListingForm(forms.ModelForm):
    class Meta:
        model=Listings
        fields = ['listing_category', 'listing_title', 'listing_image', 'listing_price']


class BidForm(forms.ModelForm):
    class Meta:
        model=Bid
        fields=['bid_price']