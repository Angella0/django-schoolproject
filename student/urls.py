# from django.conf.urls import url
from django.urls import path
# from django.urls.resolvers import URLPattern
from.views import register_student, student_list


app_name = 'student'
urlpatterns = [
    path("register",register_student, name = "register_student"),
    path("list/", student_list, name = "student_list"),
    ]
