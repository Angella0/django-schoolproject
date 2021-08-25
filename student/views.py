from django.shortcuts import redirect, render
from.models import Student
from .forms import StudentRegistrationForm
from django.shortcuts import render

def register_student(request):
    if request.method == "POST":
       form = StudentRegistrationForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('student:student_list')
       else:
           print(form.errors)

    else:
        form = StudentRegistrationForm()
    return render(request, "register_student.html", {"form":form})

def student_list(request):
    students = Student.objects.all()
    return render(request,"student_list.html", {
        "students":students
    })

# Create your views here.
