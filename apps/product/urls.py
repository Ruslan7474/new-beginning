from django.urls import path
from apps.product.views import HomeView, SearchView, ToggleWishlistView, WishlistView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('wishlist/<int:product_id>', ToggleWishlistView.as_view(), name='wishlist_toggle'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
]
