from django.urls import path
from .views import (
    StudentListView,
    ClassPeriodListView,
    CoursesListView,
    CoursesDetailsView,
    TeacherDetailsView,
    TeachersListView,
    ClassPeriodDetailView,
    ClassRoomListView,
    ClassRoomDetailsView,
   
)
from .views import (
     StudentDetailView,
)

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list_view'),
    path('students/<int:id>/', StudentDetailView.as_view(), name='student_detail_view'),  
    path('courses/', CoursesListView.as_view(), name='courses_list_view'),
    path('courses/<int:id>/', CoursesDetailsView.as_view(), name='courses_detail_view'),
    path('teachers/', TeachersListView.as_view(), name='teachers_list_view'),
    path('teachers/<int:id>/', TeacherDetailsView.as_view(), name='teachers_detail_view'),
    path('classperiod/', ClassPeriodListView.as_view(), name='classperiod_list_view'),
    path('classperiod/<int:id>/', ClassPeriodDetailView.as_view(), name='classperiod_detail_view'),
    path('classroom/', ClassRoomListView.as_view(), name='classroom_list_view'),
    path('classroom/<int:id>/', ClassRoomDetailsView.as_view(), name='classroom_detail_view'),
]





