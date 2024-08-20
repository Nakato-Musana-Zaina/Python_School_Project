from django.db import models
from django.db.models.manager import Manager
from students.models import Students


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
    stiudents = models.ManyToManyField(Students)

    

    objects = models.Manager()

def __str__(self):
    return self.courses_name
