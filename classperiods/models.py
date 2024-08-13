
from django.db import models
from courses.models import Courses
from teachers.models import Teacher
from classes.models import ClassRoom

class ClassPeriod(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=10)  



    objects = models.Manager()

    def __str__(self):
        return f'{self.course} with {self.teacher} in {self.classroom} on {self.day_of_week}'




