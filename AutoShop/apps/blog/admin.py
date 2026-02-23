from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'created_at')
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ('title', 'content')
	exclude = ('published_at',)

	def get_readonly_fields(self, request, obj=None):
		if obj is None:
			return ()
		return ('created_at', 'updated_at')
