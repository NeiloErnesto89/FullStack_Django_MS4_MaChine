from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    slug = models.SlugField("Slug", max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="product_img")

    def __str__(self):
        return self.name
