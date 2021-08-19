from django import forms
from django.forms import ModelForm, widgets
from .models import CoursesForm

class Courses(forms.ModelForm):
    
    class Meta:
        model = CoursesForm
        fields = "__all__"
        widgets ={
          'name' : forms.TextInput(attrs={'class':'form-control'}),
          'course_code' : forms.TextInput(attrs={'class':'form-control'}),
          'syllabus' : forms.TextInput(attrs={'class':'form-control'}),
          'course_trainer' : forms.TextInput(attrs={'class':'form-control'}),
          'course_schedule' : forms.TextInput(attrs={'class':'form-control'}),
          'course_duration' : forms.TextInput(attrs={'class':'form-control'}),
          
        }
