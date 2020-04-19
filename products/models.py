from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	title = models.CharField(max_length=100)
	url = models.URLField(max_length=100)
	pub_date = models.DateTimeField()
	votes_total = models.IntegerField()
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='images/')
	body = models.TextField()
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def summary(self):
		if len(self.body)>100:
			return self.body[:100]
		else:
			return self.body

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %d %Y')