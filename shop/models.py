from django.utils.translation import gettext as _
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ('-created_at',)
        index_together = (('id', 'slug'), )
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:detail', args=(self.id, self.slug))
    
    def get_price(self):
        if self.sale_price and self.sale_price < self.price:
            return self.sale_price
        return self.price
