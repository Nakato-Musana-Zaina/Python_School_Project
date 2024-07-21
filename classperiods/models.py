from django.db import models
from students.models import Students

# Create your models here.

class ClassPeriod(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE, related_name="classperiods")
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField()
    # classroom = models.ForeignKey(Classes, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=40)


    objects = models.Manager()

    def __str__(self):
         return f'{self.course}'
