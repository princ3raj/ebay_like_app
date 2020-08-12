from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


from .forms import *

from .models import User, Listings, Bid, Comments


def index(request):
    listings=Listings.objects.all()
    context={'listings':listings}
    return render(request, "auctions/index.html",context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")




def categories(request):
    listings=Listings.objects.all()
    list_item=[]
    for listing in listings:
        list_item.append(listing.listing_category)

    list_item=set(list_item)
    print(list_item)

    context={'categories':list_item}
    return render(request,"auctions/categories.html", context)



def listing(request,item_id):
    listing=Listings.objects.get(pk=item_id) 
    watchlistform=WatchListForm()   
    bids=Bid.objects.all()
    i=0
    for bid in bids:
       if str(bid.bidding)==listing.listing_title:
           i+=1

    #checking if user is the one who listed the item
    if str(request.user)==str(listing.listing_owner):
        j=1
    else:
        j=0

    print(listing.listing_title)
   

    comments=Comments.objects.all()
    comment_all=[]
    print(type(str(comments[0].listing_comment)))
    for comment in comments:
        if str(comment.listing_comment)==listing.listing_title:
            comment_all.append(comment)
            
        else:
            pass

    len_of_comments=len(comment_all)
    print(len_of_comments)
    if request.method !='POST':
        #No data submitted; create a blank form.
        form= BidForm()
        comment= CommentForm()
    
    elif request.method=='POST' and 'bid' in request.POST:        #Post data submitted; process data.
        form=BidForm(data=request.POST)
        if form.is_valid():
            new_bid=form.save(commit=False)
            new_bid.bidder=request.user
            new_bid.bidding=Listings(listing.id)
            new_bid.save()
            return redirect('index')

    if request.method !='POST':
        #No data submitted; create a blank form.
        form= BidForm()
        comment= CommentForm()
    
    elif request.method=='POST' and 'comment' in request.POST:        #Post data submitted; process data.
        comment=CommentForm(data=request.POST)
        if comment.is_valid():
            new_comment=comment.save(commit=False)
            new_comment.comment_owner=request.user
            new_comment.listing_comment=Listings(listing.id)
            new_comment.save()
            return redirect('index')

    if request.method !='POST':
        #No data submitted; create a blank form.
       pass
    
    elif request.method=='POST' and 'watchlistbutton' in request.POST:        #Post data submitted; process data.
        watchlist=WatchListForm(data=request.POST)
        if watchlist.is_valid():
            new_watchlist=watchlist.save(commit=False)
            new_watchlist.watchlist_owner=request.user
            new_watchlist.watchlist_listing=Listings(listing.id)
            new_watchlist.save()
            return redirect('index')


    
    watchlistitem=WatchList.objects.all()
    listingsitem=[]
    for listingone in watchlistitem:
        if request.user==listingone.watchlist_owner:
            listing_item=listingone.watchlist_listing
            listingsitem.append(listing_item)

    key=0

   
    for userwatchlist in listingsitem:
        if listing.listing_title==userwatchlist.listing_title:
            key= 1
        else:
            pass

    BidItems=Bid.objects.all()
    biditems=[]
    for bidone in BidItems:
        if request.user==bidone.bidder:
            bid_item=bidone.bidding
            biditems.append(bid_item)

    

    
   



    context={'listing':listing,'no_of_bids':i,'j':j,"comments":comment_all,'len':len_of_comments,
    'form':form,'commentForm':comment,'watchlistform':watchlistform,'key':key}
    return render(request,"auctions/listing.html",context)



def category_items(request, category):
        listings=Listings.objects.all()

        specific_category=[]

        for listing in listings:
            if listing.listing_category==category:
                specific_category.append(listing)

        print(specific_category)


        context={'listing':specific_category}

        return render(request, "auctions/category_items.html", context)



def create_listing(request):
    if request.method !='POST':
        #No data submitted; create a blank form.
        form= ListingForm()
    else:
        #Post data submitted; process data.
        form=ListingForm(request.POST,request.FILES)
        if form.is_valid():
            new_listing=form.save(commit=False)
            new_listing.listing_owner=request.user
            new_listing.save()
            return redirect('index')




    context={'form':form}
    return render(request,"auctions/create_listing.html",context)



def watchlist(request):

    watchlistform=WatchListForm()
    watchlist=WatchList.objects.all()
    listings=[]
    for listing in watchlist:
        if request.user==listing.watchlist_owner:
            listing_item=listing.watchlist_listing
            listings.append(listing_item)

    
        

    context={'listings':listings,'watchlistform':watchlistform}


    
    return render(request,'auctions/watchlist.html',context)