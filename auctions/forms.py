from django import forms  

from .models import Listings,Bid, WatchList, Comments


class ListingForm(forms.ModelForm):
    class Meta:
        model=Listings
        fields = ['listing_category', 'listing_title', 'listing_image', 'listing_price']


class BidForm(forms.ModelForm):
    class Meta:
        model=Bid
        fields=['bid_price']


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['comments']


class WatchListForm(forms.ModelForm):
    class Meta:
        model=WatchList
        fields=['watchlist_listing','watchlist_owner']
        exclude=['watchlist_listing','watchlist_owner']