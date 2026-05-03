from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.product.models import *



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 2


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1
    show_change_link = True


@admin.register(Product)
class ProductAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'is_available')
    list_filter = ('category', 'is_available')
    inlines = [ProductImageInline, ProductVariantInline]
    prepopulated_fields = {'slug':('name',)}


@admin.register(Category)
class CategoryAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_active')
    list_filter = ('is_active',)
    prepopulated_fields = {'slug':('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', ) 
    prepopulated_fields = {'slug':('name',)}


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'price', 'stock', 'sku')
    list_filter = ('sku',)
    filter_horizontal = ('attributes',)
  

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('brand','name', ) 


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', ) 


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('attribute', 'value') 

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')  


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('big_title', 'small_title', 'link')  

