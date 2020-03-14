from django.test import TestCase

from .models import (
    Category,
    SubCategory,
    Brand,
    GeneralProduct,
    CountableProduct,
    UnCountableProduct)

# Create your tests here.
class ProductTests(TestCase):
    category = {'category_name': 'test_category'}
    subcategory = {'subcategory_name': 'test_subcategory'}
    brand = {
        'brand_name': 'test_brand',
        'brand_website': 'www.example.com',
        'brand_description': 'brand description',
    }
    uncountable_product = {
        'product_name': 'test_uncountable_product',
        'product_description': 'description of uncountable product',
        'price_per_unit': '30000',
        'total_available_in_stock': '8',
        'is_countable': '0',
    }
    countable_product = {
        'product_name': 'test_countable_product',
        'product_description': 'description of countable product',
        'price_per_unit': '80',
        'total_available_in_stock': '0',
        'is_countable': '1',
    }

    def setUp(self):
        self.test_cat = Category.objects.create(
            category_name=self.category['category_name'])

        self.test_subcat = SubCategory.objects.create(
            parent_category=self.test_cat,
            subcategory_name=self.subcategory['subcategory_name'])

        self.test_brand = Brand.objects.create(
            brand_name=self.brand['brand_name'],
            brand_website= self.brand['brand_website'],
            brand_description=self.brand['brand_description'])

        self.test_ucproduct = GeneralProduct.objects.create(
            product_name=self.uncountable_product['product_name'],
            brand=self.test_brand,
            subcategory=self.test_subcat,
            product_description=self.uncountable_product['product_description'],
            price_per_unit=self.uncountable_product['price_per_unit'],
            total_available_in_stock=self.uncountable_product['total_available_in_stock'],
            is_countable=self.uncountable_product['is_countable']
        )

        self.test_cproduct = GeneralProduct.objects.create(
            product_name=self.countable_product['product_name'],
            brand=self.test_brand,
            subcategory=self.test_subcat,
            product_description=self.countable_product['product_description'],
            price_per_unit=self.countable_product['price_per_unit'],
            total_available_in_stock=self.countable_product['total_available_in_stock'],
            is_countable=self.countable_product['is_countable']
        )

    def test_category_created(self):
        self.assertEqual(Category.objects.all().count(), 1)
        self.assertEqual(
            self.test_cat.category_name, self.category['category_name'])

    def test_subcategory_created(self):
        self.assertEqual(SubCategory.objects.all().count(), 1)
        self.assertEqual(
            self.test_subcat.subcategory_name, self.subcategory['subcategory_name'])

    def test_brand_created(self):
        self.assertEqual(Brand.objects.all().count(), 1)
        self.assertEqual(self.test_brand.brand_name, self.brand['brand_name'])
        self.assertEqual(self.test_brand.brand_website, self.brand['brand_website'])
        self.assertEqual(
            self.test_brand.brand_description, self.brand['brand_description'])
  
    def test_general_product_created(self):
        self.assertEqual(GeneralProduct.objects.all().count(), 2)
        self.assertEqual(
            self.test_ucproduct.product_name,
            self.uncountable_product['product_name'])
        self.assertEqual(
            self.test_ucproduct.brand, self.test_brand)
        self.assertEqual(
            self.test_ucproduct.subcategory, self.test_subcat)
        self.assertEqual(
            self.test_ucproduct.product_description,
            self.uncountable_product['product_description'])
        self.assertEqual(
            self.test_ucproduct.price_per_unit,
            self.uncountable_product['price_per_unit'])
        self.assertEqual(
            self.test_ucproduct.total_available_in_stock,
            self.uncountable_product['total_available_in_stock'])
        self.assertEqual(
            self.test_ucproduct.is_countable,
            self.uncountable_product['is_countable'])

        self.assertEqual(
            self.test_cproduct.product_name,
            self.countable_product['product_name'])
        self.assertEqual(
            self.test_cproduct.brand, self.test_brand)
        self.assertEqual(
            self.test_cproduct.subcategory, self.test_subcat)
        self.assertEqual(
            self.test_cproduct.product_description,
            self.countable_product['product_description'])
        self.assertEqual(
            self.test_cproduct.price_per_unit,
            self.countable_product['price_per_unit'])
        self.assertEqual(
            self.test_cproduct.total_available_in_stock,
            self.countable_product['total_available_in_stock'])
        self.assertEqual(
            self.test_cproduct.is_countable,
            self.countable_product['is_countable'])

    def test_countable_product_detail(self):
        test_cdetail = CountableProduct.objects.create(
            product=self.test_cproduct, count='9')

        self.assertEqual(test_cdetail.product, self.test_cproduct)
        self.assertEqual(test_cdetail.count, '9')

    def test_uncountable_product_detail(self):
        uc_detail = {
            'amount': '87',
            'unit': 'gr'
        }
        test_ucdetail = UnCountableProduct.objects.create(
            product=self.test_ucproduct, 
            amount=uc_detail['amount'],
            unit=uc_detail['unit']
        )

        self.assertEqual(test_ucdetail.product, self.test_ucproduct)
        self.assertEqual(test_ucdetail.amount, uc_detail['amount'])
        self.assertEqual(test_ucdetail.unit, uc_detail['unit'])