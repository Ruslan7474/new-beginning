from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name="категория"
        verbose_name_plural="Категории"


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name="тег"
        verbose_name_plural="Теги"


class Post(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, 
        null=True, blank=True, verbose_name="Категория"
    )
    tags = models.ManyToManyField(Tag, related_name='posts')
    title = models.CharField(max_length=100, verbose_name="Название")
    img = models.ImageField(upload_to='posts/', verbose_name="Фото")
    desc = CKEditor5Field('Описание', config_name='extends')
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug}) 

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name="пост"
        verbose_name_plural="Посты"
