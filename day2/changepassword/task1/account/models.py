from django.db import models

# Create your models here.
class signup(models.Model):
	
	
	tempassword=models.CharField(max_length=50,null=True,blank=True)
	email=models.EmailField(max_length=50,unique=True)
	password=models.CharField(max_length=50)

	
	def __str__(self):
		return self.tempassword+" "+self.email+" "+self.password
	