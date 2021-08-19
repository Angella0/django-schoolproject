from django import forms
from django.forms import ModelForm, widgets
from .models import Calender

class CalenderForm(forms.ModelForm):
    
    class Meta:
        model = Calender
        fields = "__all__"
        widgets ={
          'event_name' : forms.TextInput(attrs={'class':'form-control'}),
          'event_date' : forms.TextInput(attrs={'class':'form-control'}),
          'event_planner' : forms.TextInput(attrs={'class':'form-control'}),
          'event_participation' : forms.TextInput(attrs={'class':'form-control'}),
          'event_duration' : forms.TextInput(attrs={'class':'form-control'}),
          'course_duration' : forms.TextInput(attrs={'class':'form-control'}),
           
        }