
from django.urls import path
from .views import (
    StudentListView,
    StudentDetailView,
    CoursesListView,
    CoursesDetailsView,
    TeachersListView,
    TeacherDetailsView,
    ClassPeriodListView,
    ClassPeriodDetailView,
   ClassRoomListView,
    ClassRoomDetailsView,
    ClassPeriodCreateView,
    WeeklyTimetableView,
)

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:id>/', StudentDetailView.as_view(), name='student_detail'),
    
    path('courses/', CoursesListView.as_view(), name='courses_list'),
    path('courses/<int:id>/', CoursesDetailsView.as_view(), name='courses_detail'),
    
    path('teachers/', TeachersListView.as_view(), name='teachers_list'),
    path('teachers/<int:id>/', TeacherDetailsView.as_view(), name='teacher_detail'),
    
    path('classperiods/', ClassPeriodListView.as_view(), name='classperiod_list'),
    path('classperiods/<int:id>/', ClassPeriodDetailView.as_view(), name='classperiod_detail'),
    
    path('classrooms/', ClassRoomListView.as_view(), name='classroom_list'),
    path('classrooms/<int:id>/', ClassRoomDetailsView.as_view(), name='classroom_detail'),

     path('classperiod/create/', ClassPeriodCreateView.as_view(), name='classperiod_create'),
    path('timetable/', WeeklyTimetableView.as_view(), name='weekly_timetable'),
]


