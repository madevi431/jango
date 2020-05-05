from django.db import models

# Create your models here.
class userregister(models.Model):
	fullname=models.CharField(max_length=100)
	email=models.EmailField()
	image=models.FileField(upload_to='images/')
	def __str__(self):
		return self.fullname