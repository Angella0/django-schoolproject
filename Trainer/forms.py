from django import forms
from django.forms import ModelForm, widgets
from .models import Trainer

class TrainerRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Trainer
        fields = "__all__"
        widgets ={
          'first_name' : forms.TextInput(attrs={'class':'form-control'}),
          'last_name' : forms.TextInput(attrs={'class':'form-control'}),
          'Age' : forms.TextInput(attrs={'class':'form-control'}),
          'Gender' : forms.TextInput(attrs={'class':'form-control'}),
          # 'Bio' : forms.TextInput(attrs={'class':'form-control'}),
          'Courses' : forms.TextInput(attrs={'class':'form-control'}),
          'Email_Address' : forms.TextInput(attrs={'class':'form-control'}),
          
          'Lesson_Duration' : forms.TextInput(attrs={'class':'form-control'}),
          'phone_number' : forms.TextInput(attrs={'class':'form-control'}),
  
        }
