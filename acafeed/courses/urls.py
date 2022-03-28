from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('admin-create-course/', views.courses_admincreatecourse, name="admincreatecourse"),
    path('course-home/', views.courses_coursehome, name="coursehome"),
    path('find-courses/', views.courses_findcourses, name="findcourses"),
    path('my-courses/', views.courses_mycourses, name="mycourses"),
    path('read-messages/', views.read_message, name ="readmessage"),
    path('all-messages/', views.all_messages, name="allmessages")
]
