# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Category, Products


class ProductsModelTests(TestCase):

    def test_product_category_model_is_correctly(self):
        """
        return correctly product category after creation in the database
        """
        new_product_category = Category(
            name='New Category'
        )
        self.assertIsInstance(new_product_category, Category)

    def test_products_model_is_correctly(self):
        """
        return correctly product object after creation in the database
        """
        category = Category(name='New Category')
        new_product = Products(
            name='New Product',
            category=category,
            price='0.00',
            description='New description for the new product.'
        )
        self.assertIsInstance(new_product, Products)
