from django.contrib import admin
from apps.partners.models import Partner


@admin.register(Partner)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'link') 
