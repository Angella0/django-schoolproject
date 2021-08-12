from django.shortcuts import render

from .forms import TrainerRegistrationForm
from django.shortcuts import render
# Create your views here.
def register_trainer(request):
    form = TrainerRegistrationForm
    return render(request, "register_trainer.html", {"form":form})
