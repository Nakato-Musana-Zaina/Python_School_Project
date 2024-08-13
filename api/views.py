from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# import courses
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
        country = request.query_params.get ("first_name")
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
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

    
    class StudentDetailView(APIView):
        def get(self, request, id):
            student = Students.objects.get(id=id)
            serializer = StudentSerializers(student)
            return Response(serializer.data)
        
        
        def enroll_student(self, student, course_id):
            Course = Courses.objects.get(id = course_id)
            student.courses.add(Course)

        def post(self, request, id):
            Student = Students.objects.get(id=id)
            action = request.data.get("action")
            if action == "enroll":
                course_id =request.data.get("courses")
                self.enroll_student(Student,course_id)

                return Response(status.HTTP_201_CREATED)

        def put(self, request, id):
            student = Students.objects.get(id = id)
            serializer = StudentSerializers(student, data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
            
        def delete(self, request, id):
            student = Students.objects.get(id = id)
            student.delete()
            return Response(status= status.HTTP_202_ACCEPTED)
    

class CoursesListView(APIView):
    def get(self, request):
        courses = Courses.objects.all()
        serializer = StudentSerializers(courses, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = CoursesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class CoursesDetailsView(APIView):
    def put(self,request,id):
        courses = Courses.objects.get(id = id)
        serializer = StudentSerializers(courses, data =request)
        if serializer.is_valid():
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
    
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request,id):
        courses = Students.objects.get(id=id)
        courses.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    


class TeachersListView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializers(teacher, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = TeacherSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class TeacherDetailsView(APIView):
    def put(self,request,id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializers(teacher, data =request)
        if serializer.is_valid():
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
    
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request,id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    



class ClassRoomListView(APIView):
    def get(self, request):
        classroom = ClassRoom.objects.all()
        serializer = ClassRoomSerializers(classroom, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = ClassRoomSerializers(data=request.data) # type: ignore
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class ClassRoomDetailsView(APIView):
    def put(self,request,id):
        classroom= ClassRoom.objects.get(id = id)
        serializer = ClassRoomSerializers(classroom, data =request) # type: ignore
        if serializer.is_valid():
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
    
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request,id):
        classroom = ClassRoom.objects.get(id=id)
        classroom.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    

class ClassPeriodListView(APIView):
    def get(self, request):
        classperiods = ClassPeriod.objects.all()
        serializer = ClassperiodSerializers(classperiods, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = ClassperiodSerializers(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class ClassPeriodDetailView(APIView):
    def put(self,request,id):
        classPeriod= ClassPeriod.objects.get(id = id)
        serializer = ClassperiodSerializers(classPeriod, data =request) 
        if serializer.is_valid():
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request,id):
        classPeriod = ClassPeriod.objects.get(id=id)
        classPeriod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

# class ClassesPeriodListView(APIView):
#     def get(self, request):
#         classperiods = Classes.objects.all()
#         serializer = ClassPeriodSerializers(classperiods, many=True)
#         return Response(serializer.data)
    

#     def post(self, request):
#         serializer = ClassPeriodSerializers(data=request.data) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

# class ClassPeriodDetailsView(APIView):
#     def put(self,request,id):
#         classPeriod= ClassPeriod.objects.get(id = id)
#         serializer = ClassPeriodSerializers(classPeriod, data =request) 
#         if serializer.is_valid():
#             return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
    
#         else:
#             return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
    
#     def delete(self, request,id):
#         classPeriod = ClassPeriod.objects.get(id=id)
#         classPeriod.delete()
#         return Response(status=status.HTTP_202_ACCEPTED)

    




    
    

