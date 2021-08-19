# from django.conf.urls import url
from django.urls import path
# from django.urls.resolvers import URLPattern
from.views import register_courses,course_list



urlpatterns = [
    path("register",register_courses, name = "register_courses"),
    path("list",course_list, name = "course_list"),
    ]