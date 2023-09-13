from django.db import models
from slugify import slugify


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='название категории')
    slug = models.SlugField(max_length=30, primary_key=True, blank=True)


    def __str__(self) -> str:
        return self.title
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product', verbose_name='категории')
    title = models.CharField(max_length=200, verbose_name='название', unique=True)
    slug = models.SlugField(max_length=30, primary_key=True, blank=True)
    image = models.ImageField(upload_to='images/', verbose_name='изображения')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    in_stock = models.BooleanField(default=False)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()



class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')