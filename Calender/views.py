
from django.shortcuts import render
from .forms import CalenderForm
from django.shortcuts import render
from Calender.models import Calender

def register_calender(request):
    if request.method == "POST":
       form = CalenderForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
       else:
           print(form.errors)

    else:
        form = CalenderForm()
    return render(request, "calender.html", {"form":form})


def calender_list(request):
    calenders =  Calender.objects.all()
    return render(request,"calender_list.html", {
        "calenders":calenders
    })
# Create your views here.
