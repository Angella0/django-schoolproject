from django.shortcuts import render
from student.models import Student
from Trainer.models import Trainer
from Courses.models import CoursesForm
from cal.models import Event
# Create your views here.
def home(request):
    students = Student.objects.count()
    trainers = Trainer.objects.count()
    courses = CoursesForm.objects.count
    cal = Event.objects.count()
    data = {"students": students, "traners":trainers, "courses":courses, "events": cal}
    return render(request, "home.html", data)