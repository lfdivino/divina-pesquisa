# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)


class Products(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=False
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=255)
