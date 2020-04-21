from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class Votes(models.Model):
	voter = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __str__(self):
		return self.voter.username + ' voted ' + self.product.title