# students/models.py
from django.db import models

class Students(models.Model):
    students_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    code = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField()
    nextOfKin = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='photos/')
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
   

    objects = models.Manager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
