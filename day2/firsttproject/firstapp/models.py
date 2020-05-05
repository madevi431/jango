from django.db import models

# Create your models here.
class Emp(models.Model):
	first_name=models.CharField(max_length=50,null=True)
	last_name=models.CharField(max_length=50)
	age=models.IntegerField(null=True)
	def __str__(self):
		return self.first_name+" "+self.last_name+" "+self.age

