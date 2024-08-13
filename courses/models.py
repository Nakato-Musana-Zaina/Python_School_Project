from django.db import models
from django.apps import apps

# Create your models here.
class Courses(models.Model):
    courses_name = models.CharField(max_length=20)
    courses_id = models.AutoField(primary_key=True)  
    courses_code = models.SmallIntegerField()
    courses_instructor = models.CharField(max_length=20)  
    courses_assignment = models.CharField(max_length=20)
    courses_level = models.CharField(max_length=20)
    courses_department = models.CharField(max_length=20)
    courses_syllabus = models.CharField(max_length=20)
    courses_exams = models.CharField(max_length=20)
    courses_term = models.CharField(max_length=10)

    objects = models.Manager()

    def get_students(self):
        Students = apps.get_model('students', 'Students')
        return Students.objects.all()
    
    def __str__(self):
        return f'{self.courses_name}'


# from django.db import models
# from students.models import Students
# from django.apps import apps


# # Create your models here.
# class Courses(models.Model):
#     courses_name=models.CharField(max_length=20)
#     courses_id = models.AutoField()
#     courses_code=models.SmallIntegerField()
#     courses_instuctor=models.CharField(max_length=20)
#     courses_assignment=models.CharField(max_length=20)
#     courses_level=models.CharField(max_length=20)
#     courses_department=models.CharField(max_length=20)
#     courses_syllabus=models.CharField(max_length=20)
#     courses_exams=models.CharField(max_length=20)
#     courses_term=models.CharField(max_length=10)

#     objects = models.Manager()

#     def get_students(self):
#         Students = apps.get_model('students', 'Students')
#         return Students.objects.all()
    
#     def __str__(self):
#          return f'{self.courses_name}'
