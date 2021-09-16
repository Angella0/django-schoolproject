from django.urls.conf import include, path
from rest_framework import routers
from .views import StudentViewSet
from .views import TrainerViewSet
from .views import CalViewSet
from .views import CoursesViewSet

router =routers.DefaultRouter()
router.register("students/", StudentViewSet)
router.register("trainer/", TrainerViewSet)
router.register("cal/", CalViewSet)
router.register("courses/", CoursesViewSet)

app = "api"
urlpatterns= [
    path("", include(router.urls)),
]