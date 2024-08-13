from django.apps import apps
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
    courses = models.ManyToManyField('courses.Courses', related_name='students')

    objects = models.Manager()

    def get_courses(self):
        Courses = apps.get_model('courses', 'Courses')
        return Courses.objects.all()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# from django.db import models
# from courses.models import Courses
# from classes.models import ClassRoom

# class Students(models.Model):
#     students_id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     email = models.EmailField()
#     code = models.PositiveSmallIntegerField()
#     date_of_birth = models.DateField()
#     country = models.CharField(max_length=20)
#     bio = models.TextField()
#     age = models.PositiveSmallIntegerField()
#     nextOfKin = models.CharField(max_length=20)
#     picture = models.ImageField(upload_to='photos/')
#     created_on = models.DateField(auto_now_add=True)
#     updated_on = models.DateField(auto_now=True)  
#     courses = models.ManyToManyField(Courses, related_name='students')
#     classes = models.ManyToManyField(ClassRoom, related_name='students')

#     objects = models.Manager()

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'







