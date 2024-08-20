# from rest_framework import serializers
from rest_framework import serializers;
from students.models import Students
from courses.models import Courses
from classperiods.models import ClassPeriod
from teachers.models import Teacher
from classes.models import ClassRoom



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

class StudentSerializers(serializers.ModelSerializer):
      courses = CoursesSerializers(many= True)
      class Meta:
            model=Students
            fields='__all__'



class ClassRoomSerializers(serializers.ModelSerializer):
      class Meta:
            model = ClassRoom
            fields='__all__'   



#customizing the searlizer
class ListStudentSerializers(serializers.ModelSerializer):
      class Meta:
            model = Students
            fields=["FirstName"]  


class minimalStudentSerializers(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model=Students
        fields=["full_name","email"] 


class minimalTeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self, object):
        return f"{object.teacher_name}"

    class Meta:
          model = Teacher
          fields = ["teacher_hobby", "teacher_occupation", "full_name"]   


class minimalCourseSerializer(serializers.ModelSerializer):
    courses_name = serializers.SerializerMethodField()
    def get_courses_name(self, object):
        return f"{object.courses_name}"

    class Meta:
          model = Teacher
          fields = ["courses_name"]  

class minimalClassPeriodSerializer(serializers.ModelSerializer):
    day = serializers.SerializerMethodField()
    def get_course_name(self, object):
        return f"{object.day_of_week}"

    class Meta:
          model = Teacher
          fields = ["day", "start_time"]  


class minimalClassRoomSerializer(serializers.ModelSerializer):
    classroom = serializers.SerializerMethodField()
    def get_course_name(self, object):
        return f"{object.class_name}"

    class Meta:
          model = Teacher
          fields = ["classroom", "class_rep"]  



