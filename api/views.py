from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets


# import courses
from students.models import Students
from classes.models import ClassRoom
from teachers.models import Teacher
from courses.models import Courses
from classperiods.models import ClassPeriod

from .serializer import TeacherSerializers
from .serializer import ClassperiodSerializers
from .serializer import ClassRoomSerializers
from .serializer import StudentSerializers
from .serializer import CoursesSerializers


class StudentListView(APIView):
    def get(self, request):
        students = Students.objects.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class StudentDetailsView(APIView):
    def put(self,request,id):
        student = Students.objects.get(id = id)
        serializer = StudentSerializers(student, data =request)
        if serializer.is_valid():
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
    
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request,id):
        student = Students.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    

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
    



class ClassesPeriodListView(APIView):
    def get(self, request):
        classperiods = Classes.objects.all()
        serializer = ClassPeriodSerializers(classperiods, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = ClassPeriodSerializers(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class ClassPeriodDetailsView(APIView):
    def put(self,request,id):
        classPeriod= ClassPeriod.objects.get(id = id)
        serializer = ClassPeriodSerializers(classPeriod, data =request) 
        if serializer.is_valid():
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
    
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request,id):
        classPeriod = ClassPeriod.objects.get(id=id)
        classPeriod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    




    
    

