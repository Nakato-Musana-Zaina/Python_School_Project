from django.db import models
from django.apps import apps

# Create your models here.
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
    updated_on = models.DateField(auto_now=True)  # Changed to auto_now for updates
    courses = models.ManyToManyField('courses.Courses', related_name='students')

    objects = models.Manager()

    def get_courses(self):
        # This method is not strictly necessary if you're just accessing courses
        Courses = apps.get_model('courses', 'Courses')
        return Courses.objects.all()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'



# from django.db import models
# from django.apps import apps


# from courses.models import Courses

# # Create your models here.
# class Students(models.Model):
#     students_id = models.AutoField(primary_key=True)
#     first_name=models.CharField(max_length=20)
#     last_name=models.CharField(max_length=20)
#     email=models.EmailField()
#     code=models.PositiveSmallIntegerField()
#     date_of_birth=models.DateField()
#     country=models.CharField(max_length=20)
#     bio=models.TextField()
#     age = models.PositiveSmallIntegerField()
#     nextOfKin = models.CharField(max_length=20)
#     picture = models.ImageField(upload_to='photos/')
#     created_on = models.DateField(auto_now_add=True)
#     updated_on = models.DateField(auto_now_add=True)
#     courses = models.ManyToManyField('courses.Courses', related_name='students')

#     objects = models.Manager()

#     def get_courses(self):
#         Courses = apps.get_model('courses', 'Courses')
#         return Courses.objects.all()
    
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'