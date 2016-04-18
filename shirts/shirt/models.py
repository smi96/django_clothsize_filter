from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.
CHOICES = (('Xtra-Small','Xtra-Small'),
               ('Small','Small'),
               ('Medium','Medium'),
               ('Large','Large'),
               ('Xtra-Large','Xtra-Large'),	)

class Product(models.Model):
	product_name = models.CharField(max_length=120)
	product_id = models.ForeignKey('Sno')
	product_price = models.IntegerField(default=0)
	price_url = models.URLField()
	#size = models.ForeignKey(Size)
	def __str__(self):
		return str(self.product_id)


class Product_Varients(models.Model):
	size = models.CharField(max_length=20, choices=CHOICES, default='Small')
	product_id = models.ForeignKey('Sno')
	SKU_Code = models.CharField(max_length=20)
	def __str__(self):
		return str(self.product_id)

class Sno(models.Model):
	product_id = models.IntegerField(default=0)


	def __str__(self):
		return str(self.product_id)