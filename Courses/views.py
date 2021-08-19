from Courses.models import CoursesForm
from django.shortcuts import render
from .forms import Courses
from django.shortcuts import render

def register_courses(request):
    if request.method == "POST":
       form = Courses(request.POST, request.FILES)
       if form.is_valid():
           form.save()
       else:
           print(form.errors)

    else:
        form = Courses()
    return render(request, "courses.html", {"form":form})


def course_list(request):
    courses =  CoursesForm.objects.all()
    return render(request,"courses_list.html", {
        "courses":courses
    })
# Create your views here.
