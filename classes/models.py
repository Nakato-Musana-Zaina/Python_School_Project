# classes/models.py
from django.db import models

class ClassRoom(models.Model):
    class_time = models.IntegerField()
    class_capacity = models.IntegerField()
    class_name = models.CharField(max_length=50)
    class_lecture = models.CharField(max_length=50)
    class_id = models.AutoField(primary_key=True)
    class_rep = models.CharField(max_length=50)
    class_description = models.TextField()
    class_attendance = models.IntegerField()
    location = models.CharField(max_length=100, blank=True, null=True)
    is_available = models.BooleanField(default=True)
    schedule = models.TextField(blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.class_name}'
