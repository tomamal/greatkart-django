from django.urls import reverse
from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=50, unique=True)
    cat_slug = models.SlugField(max_length=100, unique=True)
    cat_desc = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.cat_slug])

    def __str__(self):
        return self.cat_name
