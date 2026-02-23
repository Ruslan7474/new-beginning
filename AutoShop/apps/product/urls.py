from django.urls import path
from apps.product.views import HomeView
from .views import (
    CategoryListView, ProductListView,
    ProductDetailView, ReviewCreateView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('category/<slug:category_slug>/', ProductListView.as_view(), name='product_by_category'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('<slug:slug>/review/', ReviewCreateView.as_view(), name='add_review')
]
