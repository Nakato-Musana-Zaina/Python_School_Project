# from rest_framework import serializers
from rest_framework import serializers;
from students.models import Students
from courses.models import Courses
from classperiods.models import ClassPeriod
from teachers.models import Teacher
from classes.models import ClassRoom

class StudentSerializers(serializers.ModelSerializer):
      class Meta:
            model=Students
            fields='__all__'

class TeacherSerializers(serializers.ModelSerializer):
      class Meta:
            models = Teacher
            feilds = '__all__'

class ClassperiodSerializers(serializers.ModelSerializer):
      class Meta:
            models = ClassPeriod
            feilds = '__all__'

class CoursesSerializers(serializers.ModelSerializer):
      class Meta:
            model = Courses
            fields='__all__'

class ClassRoomSerializers(serializers.ModelSerializer):
      class Meta:
            model = ClassRoom
            fields='__all__'       


     