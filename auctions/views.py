from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from .forms import *
from .models import User, Listings, Bid, Comments,WinnerList
from django.contrib.auth.decorators import login_required


def index(request):
    loggedinuser=str(request.user)
    listings=Listings.objects.all()
    winnerslist=WinnerList.objects.all()
    winners=[]
    for winner in winnerslist:
        winners.append(winner.winnername)

    
   


    context={'listings':listings,'winners':winners,'loggedinuser':loggedinuser}
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

@login_required
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



@login_required
def categories(request):
    listings=Listings.objects.all()
    list_item=[]
    for listing in listings:
        list_item.append(listing.listing_category)

    list_item=set(list_item)
    print(list_item)

    context={'categories':list_item}
    return render(request,"auctions/categories.html", context)


@login_required
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

    

    BidItems=Bid.objects.all()
    biditems=[]

    for bidone in BidItems:
            if  str(bidone.bidding)==listing.listing_title:
                bid_item=bidone
                biditems.append(bid_item)

    bidlen=len(biditems)-1
    if bidlen ==-1:
        HighestBidMade=0
        HighestBidder=None
        flag=False
    else:
        HighestBidMade=biditems[bidlen].bidstart
        HighestBidder=biditems[bidlen].bidder
        flag=True

   

    
    print(HighestBidder)
    print(listing.id)

    comments=Comments.objects.all()
    comment_all=[]
    for comment in comments:
        if str(comment.listing_comment)==listing.listing_title:
            comment_all.append(comment)
            
        else:
            pass

    len_of_comments=len(comment_all)






    if request.method=='POST' and 'bid' in request.POST:
        if flag:
            if float(request.POST['bidstart']) < biditems[bidlen].bidstart:
                  return render(request,"auctions/lessthanpreviousbids.html")
            else:
                pass

   
   

    if request.method !='POST':
        form= BidForm()
    elif request.method=='POST' and 'bid' in request.POST: 
                
                if float(request.POST['bidstart']) < listing.listing_price or float(request.POST['bidstart']) == listing.listing_price:
                    return render(request,"auctions/startbiderror.html")

                else:
    
                            form=BidForm(request.POST)
                            form.is_valid()
                            new_bid=form.save(commit=False)
                            new_bid.bidder=request.user
                            new_bid.bidding=Listings(listing.id)
                            new_bid.save()
                            return redirect('index')

   
            
                
    if request.method !='POST':
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
        if  str(bidone.bidding)==listing.listing_title:
            bid_item=bidone
            biditems.append(bid_item)

  
   

    

    
   



    context={'listing':listing,'no_of_bids':i,'j':j,"comments":comment_all,'len':len_of_comments,
    'form':form,'commentForm':comment,'watchlistform':watchlistform,
    'key':key,'highestbid':HighestBidMade,'flag':flag,'highestbidder':HighestBidder}
    return render(request,"auctions/listing.html",context)


@login_required
def category_items(request, category):
        listings=Listings.objects.all()

        specific_category=[]

        for listing in listings:
            if listing.listing_category==category:
                specific_category.append(listing)

        print(specific_category)


        context={'listing':specific_category}

        return render(request, "auctions/category_items.html", context)


@login_required
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


@login_required
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

@login_required
def delete(request,item_id,highest_bidder):
    listing=Listings.objects.get(pk=item_id)
    winner=highest_bidder

    if request.method !='POST':

        form= WinnerForm()
    
    else: 
        form=WinnerForm(data=request.POST)
        if form.is_valid():
            listing=Listings.objects.get(pk=item_id)
            new_winner=form.save(commit=False)
            new_winner.winnername=winner
            # new_winner.winnerreference=listing
            new_winner.save()
            listing.delete()
            return redirect('index')
    context={'form':form,'item_id':item_id,'highest_bidder':highest_bidder}
    return render(request,"auctions/delete.html",context)



def removewatchlist(request, item_id):
    watchlist=WatchList.objects.all()

    #deriving the name of the product that's clicked out as to remove itself
    listing=Listings.objects.get(pk=item_id)

    #logic is first i am checking that the user is deleting its own item not
    #others, then i am matching the watchlist item name with the listing item_id that
    #represents a product itself
    for watchlistitem in watchlist:
        if str(watchlistitem.watchlist_owner)==str(request.user):
            if str(watchlistitem.watchlist_listing)==str(listing):
                   watchlistitem.delete()

    # print(listing)
    # print(type(str(item_id)))
    # print(type(str(watchlist[0].watchlist_listing)))
    # print(type(str(watchlist[0].watchlist_owner)))
    # print(watchlist[0].id)
    # print(watchlist[1].id)
    # print(watchlist[2].id)
    # print(type(str(request.user)))
    # watchlist.delete()
    return redirect('index')





