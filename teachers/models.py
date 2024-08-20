# teachers/models.py
from django.db import models

class Teacher(models.Model):
    teacher_age = models.IntegerField()
    teacher_name = models.CharField(max_length=50)
    teacher_id = models.AutoField(primary_key=True)
    teacher_description = models.TextField()
    teacher_occupation = models.CharField(max_length=50)
    teacher_salary = models.IntegerField()
    teacher_hobby = models.CharField(max_length=50)
    teacher_gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    classes = models.ManyToManyField('classes.ClassRoom', related_name='teachers')

    objects = models.Manager()

def __str__(self):
    return self.teacher_name
