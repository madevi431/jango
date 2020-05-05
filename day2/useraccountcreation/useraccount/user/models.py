from django.db import models

# Create your models here.
class candidate(models.Model):
	
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	user_name=models.CharField(max_length=25)
	password=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	contact=models.IntegerField()  
	age=models.IntegerField()
	def __str__(self):
		return self.first_name+" "+self.last_name+" "+self.user_name+" "+self.password+" "+self.email+" "+str(self.contact)+" "+str(self.age)