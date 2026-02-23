from django.db import models


class Blog(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True)
	content = models.TextField(blank=True)
	image = models.ImageField(upload_to='blog/', null=True, blank=True)
	image_url = models.URLField(max_length=500, blank=True)
	published_at = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Blog'
		verbose_name_plural = 'Blogs'
		ordering = ['-created_at']

	def __str__(self):
		return self.title
