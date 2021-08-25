from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import register_trainer, trainer_list

app_name = 'trainer'
urlpatterns = [
    path("register/",register_trainer, name = "register_trainer"),
    path("list/",trainer_list, name = "trainer_list"),
    ]
