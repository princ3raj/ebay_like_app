from django.urls import path, include

from . import views

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listings/<int:item_id>/",views.listing,name="listing"),
    path("categories",views.categories,name="categories"),
    path("category_items/<str:category>/", views.category_items,name="category_items"),
    path("create_listing", views.create_listing,name="create_listing"),
    path("watchlist", views.watchlist,name="watchlist"),
    path("delete/<int:item_id>/<str:highest_bidder>/",views.delete,name="delete"),
    path("removewatchlist/<int:item_id>/",views.removewatchlist,name="remove"),
    
]
