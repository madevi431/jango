from django.db import models

# Create your models here.
class upload(models.Model):
	gender_vals = [('Male','Male'),('FeMale','FeMale')]
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	emailId = models.EmailField(null = True)
	phoneNo = models.CharField(max_length=10,)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=10,choices=gender_vals)
	date_of_birth = models.DateField(null=True)
	image = models.ImageField(upload_to='photos/')
	def __str__(self):
		return self.firstName+" "+str(self.image)

   