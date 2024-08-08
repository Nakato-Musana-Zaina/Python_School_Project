from django.db import models
from students.models import Students

# Create your models here.
class Courses(models.Model):
    students_id = models.ForeignKey(Students,on_delete=models.CASCADE,related_name='courses')
    courses_name=models.CharField(max_length=20)
    courses_code=models.SmallIntegerField()
    courses_instuctor=models.CharField(max_length=20)
    courses_assignment=models.CharField(max_length=20)
    courses_level=models.CharField(max_length=20)
    courses_department=models.CharField(max_length=20)
    courses_syllabus=models.CharField(max_length=20)
    courses_exams=models.CharField(max_length=20)
    courses_term=models.CharField(max_length=10)

    objects = models.Manager()
    
    def __str__(self):
         return f'{self.courses_name}'
