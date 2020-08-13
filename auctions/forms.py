from django import forms  

from .models import Listings,Bid, WatchList, Comments, WinnerList




class ListingForm(forms.ModelForm):
    class Meta:
        model=Listings
        fields = ['listing_category', 'listing_title', 'listing_image', 'listing_price']


class BidForm(forms.ModelForm):


    class Meta:
        model=Bid
        fields=['bidstart']

    # def clean_bidstart(self,*args,**kwargs):
    #     bidstart=self.cleaned_data.get("bidstart")
    #     if bidstart < 67 or bidstart==67:
    #         raise forms.ValidationError("Value is to small")
    #     return bidstart

 
       

        

    


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['comments']


class WatchListForm(forms.ModelForm):
    class Meta:
        model=WatchList
        fields=['watchlist_listing','watchlist_owner']
        exclude=['watchlist_listing','watchlist_owner']


class WinnerForm(forms.ModelForm):

    class Meta:
        model=WinnerList
        fields=['winnername']
        exclude=['winnername']


# #Bidding Value cheking
# def BidValueChecking():
        # BidItems=Bid.objects.all()
        # biditems=[]
        # for bidone in BidItems:
        #     if  str(bidone.bidding)==listing.listing_title:
        #         bid_item=bidone
        #         biditems.append(bid_item)

        # bidlen=len(biditems)-1

        