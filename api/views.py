from Courses.models import CoursesForm
from cal.models import Event
from Trainer.models import Trainer
from django.shortcuts import render
from student.models import Student
from rest_framework import viewsets
from .serializer import StudentSerializers
from .serializer import TrainerSerializers
from .serializer import CalSerializers
from .serializer import CoursesSerializers

# Create your views here.




class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class = StudentSerializers

class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class = TrainerSerializers

class CalViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class = CalSerializers

class CoursesViewSet(viewsets.ModelViewSet):
    queryset=CoursesForm.objects.all()
    serializer_class = CoursesSerializers
