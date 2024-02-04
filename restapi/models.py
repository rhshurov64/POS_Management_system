from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length = 1000)
    school = models.CharField(max_length = 1000)
    address = models.CharField(max_length = 1000)
    
    def __str__(self):
        return self.name