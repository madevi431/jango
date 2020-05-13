from django.db import models

# Create your models here.
class upload(models.Model):
    Name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.Name+self.image