from django.views.generic import TemplateView, ListView
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q 
from django.db.models import Prefetch

from apps.product.utils import get_wishlist
from apps.product.models import  Category, Product, Slider, WishlistItem, Brand, CarModel
from apps.blog.models import Post
from apps.partners.models import Partner


class WishlistView(TemplateView):
    template_name = 'pages/wishlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        wishlist = get_wishlist(self.request)
        context['wishlist'] = wishlist
        return context 


class ToggleWishlistView(View):
    def post(self, request, product_id):
        wishlist = get_wishlist(request)
        product = get_object_or_404(Product, id=product_id)
        item = WishlistItem.objects.filter(
            wishlist=wishlist,
            product=product
        ).first()
        if item:
            item.delete()
        else:
            WishlistItem.objects.create(
                wishlist=wishlist,
                product=product,
            )
        return redirect(request.META.get('HTTP_REFERER', '/'))
    

class SearchView(ListView):
    template_name = 'pages/search.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            return Product.objects.none()
        return Product.objects.filter(
            Q(name__icontains=query) | 
            Q(category__name__icontains=query) |
            Q(car_models__brand__name__icontains=query)
        ).distinct().prefetch_related('images')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['categories'] = Category.objects.filter(
            is_active=True,
            parent__isnull=True
        ).prefetch_related('children')
        context['category_limit'] = 8
        
        context['products'] = Product.objects.filter(is_available=True)[:8]
        context['partners'] = Partner.objects.all()
        context['sliders'] = Slider.objects.all()
        context['posts']=(
            Post.objects.prefetch_related('tags')
        )
        return context


class CategoryView(ListView):
    template_name = 'pages/category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        categories = category.get_descendants(include_self=True)
        return Product.objects.filter(
            category__in=categories
        ).prefetch_related('images')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(
            Category, slug=self.kwargs['slug']
        )
        return context
    

class BrandView(ListView):
    template_name = 'pages/brand.html'
    context_object_name = 'products'

    def get_queryset(self):
        marka = get_object_or_404(Brand, slug=self.kwargs['slug'])
        
        return Product.objects.filter(
            car_models__marka=marka,
        ).distinct().prefetch_related('images')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()[:8]
        context['brand'] = get_object_or_404(
            Brand, slug=self.kwargs['slug']
        )
        return context