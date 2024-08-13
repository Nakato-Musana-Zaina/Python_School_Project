from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from students.models import Students
from classes.models import ClassRoom
from teachers.models import Teacher
from courses.models import Courses
from classperiods.models import ClassPeriod

from .serializer import TeacherSerializers, ClassperiodSerializers, ClassRoomSerializers, StudentSerializers, CoursesSerializers

class StudentListView(APIView):
    def get(self, request):
        students = Students.objects.all()
        first_name = request.query_params.get("first_name")
        country = request.query_params.get("country")  # Fixed key
        if first_name:
            students = students.filter(first_name=first_name)
        if country:
            students = students.filter(country=country)
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get(self, request, id):
        student = Students.objects.get(id=id)
        serializer = StudentSerializers(student)
        return Response(serializer.data)
    
    def post(self, request, id):
        student = Students.objects.get(id=id)
        action = request.data.get("action")

        if action == "enroll":
            course_id = request.data.get("course_id")
            course = Courses.objects.get(id=course_id)
            student.courses.add(course)
            return Response(status=status.HTTP_200_OK)
        
        elif action == "add_to_class":
            class_id = request.data.get("class_id")
            classroom = ClassRoom.objects.get(id=class_id)
            student.classes.add(classroom)
            return Response(status=status.HTTP_200_OK)
    
    def put(self, request, id):
        student = Students.objects.get(id=id)
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        student = Students.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CoursesListView(APIView):
    def get(self, request):
        courses = Courses.objects.all()
        serializer = CoursesSerializers(courses, many=True)  # Fixed serializer
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CoursesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CoursesDetailsView(APIView):
    def put(self, request, id):
        course = Courses.objects.get(id=id)
        serializer = CoursesSerializers(course, data=request.data)  # Fixed serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        course = Courses.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeachersListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializers(teachers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailsView(APIView):
    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializers(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")
        
        if action == "assign_course":
            course_id = request.data.get("course_id")
            course = Courses.objects.get(id=course_id)
            teacher.courses.add(course)
            return Response(status=status.HTTP_200_OK)
        
        elif action == "assign_class":
            class_id = request.data.get("class_id")
            classroom = ClassRoom.objects.get(id=class_id)
            teacher.classes.add(classroom)
            return Response(status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ClassRoomListView(APIView):
    def get(self, request):
        classrooms = ClassRoom.objects.all()
        serializer = ClassRoomSerializers(classrooms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassRoomSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ClassRoomDetailsView(APIView):
    def put(self, request, id):
        classroom = ClassRoom.objects.get(id=id)
        serializer = ClassRoomSerializers(classroom, data=request.data)  # Fixed request data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        classroom = ClassRoom.objects.get(id=id)
        classroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClassPeriodListView(APIView):
    def get(self, request):
        classperiods = ClassPeriod.objects.all()
        serializer = ClassperiodSerializers(classperiods, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassperiodSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassPeriodDetailView(APIView):
    def put(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        serializer = ClassperiodSerializers(class_period, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        class_period.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClassPeriodCreateView(APIView):
    def post(self, request):
        serializer = ClassperiodSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WeeklyTimetableView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        data = []

        for period in class_periods:
            data.append({
                'course': period.course.courses_name,
                'teacher': period.teacher.teacher_name,
                'classroom': period.classroom.class_name,
                'start_time': period.start_time,
                'end_time': period.end_time,
                'day_of_week': period.day_of_week
            })
        
        return Response(data, status=status.HTTP_200_OK)
