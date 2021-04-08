from django.db import models



# Create your models here.
class Donator(models.Model):
    name = models.CharField(max_length=250)
    email=models.EmailField()
    

    def __str__(self):
        return self.name