from django.db import models

class Brands(models.Model):
    brand_name = models.CharField(max_length=20, default="brand name")
    image = models.ImageField(blank=True, null=True, default="static/home/brand/br1.png/", upload_to="images/brands/")

    def __str__(self):
        return self.brand_name


