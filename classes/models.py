from django.db import models

class ClassRoom(models.Model):
    students_id = models.ForeignKey('students.Students', on_delete=models.CASCADE, related_name="classes")
    class_time = models.IntegerField()
    class_capacity = models.IntegerField()
    class_name = models.CharField(max_length=20)
    class_lecture = models.CharField(max_length=20)
    class_id = models.IntegerField()
    class_rep = models.CharField(max_length=20)
    class_description = models.TextField()
    class_attendance = models.IntegerField()
    class_activity = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return f'{self.class_name}'



# from django.db import models
# from students.models import Students

# class ClassRoom(models.Model):
#     class_time = models.IntegerField()
#     class_capacity = models.IntegerField()
#     class_name = models.CharField(max_length=20)
#     class_lecture = models.CharField(max_length=20)
#     class_id = models.AutoField(primary_key=True)
#     class_rep = models.CharField(max_length=20)
#     class_description = models.TextField()
#     class_attendance = models.IntegerField()
#     class_activity = models.CharField(max_length=20)
#     students = models.ManyToManyField(Students, related_name='classrooms', blank=True)

#     objects = models.Manager()

#     def __str__(self):
#         return f'{self.class_name}'


