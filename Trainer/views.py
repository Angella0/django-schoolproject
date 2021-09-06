from django.shortcuts import render, redirect
from.models import Trainer
from .forms import TrainerRegistrationForm
from django.shortcuts import render
# Create your views here.
def register_trainer(request):
    if request.method == "POST":
       form = TrainerRegistrationForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('trainer:trainer_list')
       else:
           print(form.errors)

    else:
        form = TrainerRegistrationForm()
    return render(request, "register_trainer.html", {"form":form})

def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request,"trainer_list.html", {
        "trainers":trainers
    })

def trainer_profile(request, id):
    trainer = Trainer.objects.get(id=id)
    return render(request, "trainer_profile.html", {"trainer":trainer})

def trainer_edit(request, id):
    trainer = Trainer.objects.get(id=id)
    if request.method=="POST":
        form = TrainerRegistrationForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect("trainer_profile", id = trainer.id)
        else:
            form = TrainerRegistrationForm(instance=trainer)
            return render(request, "trainer_edit.html", {"form":form})


       
  