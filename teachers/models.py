from django.db import models;
from students.models import Students

# Create your models here.
class Teacher(models.Model):
    students_id = models. ForeignKey(Students, on_delete=models.CASCADE,related_name="teachers")
    teacher_age=models.IntegerField()
    teacher_name=models.CharField(max_length=20)
    teacher_id=models.IntegerField()
    teacher_course=models.CharField(max_length=20)
    teacher_class=models.CharField(max_length=20)
    teacher_description=models.CharField(max_length=20)
    teacher_occupation=models.CharField(max_length=20)
    teacher_salary=models.IntegerField()
    teacher_hobby=models.CharField(max_length=20)
    teacher_gender=models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return f'{self.teacher_description}'
