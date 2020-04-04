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
        Brand, on_delete=models.SET_NULL,
        blank=True, null=True
    )
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL,
        blank=True, null=True
    )    
    product_description = models.TextField(editable=True, blank=True, null=True)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_available_in_stock = models.PositiveIntegerField(default=0)
    is_countable = models.BooleanField(default=1)
    product_img1 = models.ImageField(upload_to='products/', blank=True, null=True)
    product_img2 = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.product_name
    

class UnCountableProduct(models.Model):
    MEASURES = [
        ('kg', 'kilograms'),
        ('gr', 'grams'),
        ('l', 'liter'),
        ('ml', 'mililiter')
    ]
    product = models.ForeignKey(GeneralProduct, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=2, choices=MEASURES, default='kg')

    def __str__(self):
        return self.product.product_name
    


class CountableProduct(models.Model):
    product = models.ForeignKey(GeneralProduct, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.product.product_name
    