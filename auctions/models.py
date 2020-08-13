from django.contrib.auth.models import AbstractUser
from django.db import models




from django.conf import settings


class User(AbstractUser):
     pass
    

class Listings(models.Model):
    CategoryType = models.TextChoices('CategoryType', 'Electronics Clothing Education Digital')
    listing_owner=models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, null=True)
    listing_title=models.CharField(max_length=100,unique=True)
    listing_image=models.ImageField(null=True,blank=True)
    listing_price=models.DecimalField(max_digits=5,decimal_places=2)
    listing_category=models.CharField(blank=True,choices=CategoryType.choices, max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.listing_title

    

   
   

    @property
    def imageURL(self):
        try:
            url=self.listing_image.url
        except:
            url=''
        return url





class Bid(models.Model):
    bidder=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    bidding=models.ForeignKey(Listings,on_delete=models.CASCADE, null=True)
    bidstart=models.DecimalField(max_digits=5,decimal_places=2)
    

    def __str__(self):
        return str(self.bidding)


class Comments(models.Model):
    listing_comment=models.ForeignKey(Listings,on_delete=models.CASCADE,null=True)
    comment_owner=models.ForeignKey(User,on_delete=models.CASCADE)
    comments=models.TextField()

    def __str__(self):
        return str(self.comments)


class WatchList(models.Model):
    watchlist_listing=models.ForeignKey(Listings,on_delete=models.CASCADE,null=True)
    watchlist_owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.watchlist_owner)
    

class WinnerList(models.Model):
    winnername=models.CharField(max_length=200)
   

    def __str__(self):
        return self.winnername