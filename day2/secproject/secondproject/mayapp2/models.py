from django.db import models

# Create your models here.
class Student(models.Model):
	branches=[('CSE','cse'),
			  ('ECE','ece'),
			  ('IT','it'),
			  ('EEE','eee')]
	stuid=models.CharField(max_length=10)
	stuname=models.CharField(max_length=50)
	branch=models.CharField(max_length=50,choices=branches)
	age=models.IntegerField()
	def __str__(self):
		return self.stuid+" "+self.stuname+" "+self.branch+" "+str(self.age)


