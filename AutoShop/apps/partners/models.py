from django.db import models


class Partner(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='partners/', null=True, blank=True)
	image_url = models.URLField(max_length=500, blank=True)
	url = models.URLField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Partner'
		verbose_name_plural = 'Partners'
		ordering = ['name']

	def __str__(self):
		return self.name
