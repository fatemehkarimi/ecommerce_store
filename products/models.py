from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=100)


    def __str__(self):
        return self.subcategory_name
    

class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    brand_logo = models.ImageField(
        upload_to='brand_logo/', blank=True, null=True
    )
    brand_website = models.CharField(max_length=255, blank=True, null=True)
    brand_description = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.brand_name
    

class GeneralProduct(models.Model):
    product_name = models.CharField(max_length=255)
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_DEFAULT,
        default='Unknown'
    )
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_DEFAULT,
    default='Unknown'
    )    
    product_description = models.TextField(editable=True, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
