# classperiods/models.py
from django.db import models
from courses.models import Courses
from teachers.models import Teacher
from classes.models import ClassRoom

class ClassPeriod(models.Model):
    DAY_OF_WEEK_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    courses = models.ManyToManyField('courses.Courses', related_name='classes')
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=9, choices=DAY_OF_WEEK_CHOICES)

    objects = models.Manager()

    def __str__(self):
        return f'The class is on {self.day_of_week}'
