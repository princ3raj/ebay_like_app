from django.contrib import admin

from .models import Listings, User, Bid, Comments, WatchList,WinnerList

from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Listings)
admin.site.register(User,UserAdmin)

admin.site.register(Bid)
admin.site.register(Comments)
admin.site.register(WatchList)
admin.site.register(WinnerList)


