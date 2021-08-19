from django.urls import path
# from django.urls.resolvers import URLPattern
from.views import register_calender, calender_list



urlpatterns = [
    path("register/",register_calender, name = "register_calender"),
    path("list/",calender_list, name = "calender_list"),


    ]