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
          'age' : forms.TextInput(attrs={'class':'form-control'}),
          'gender' : forms.TextInput(attrs={'class':'form-control'}),
          # 'Bio' : forms.TextInput(attrs={'class':'form-control'}),
          'courses' : forms.TextInput(attrs={'class':'form-control'}),
          'email_address' : forms.TextInput(attrs={'class':'form-control'}),
          # 'cv' : forms.TextInput(attrs={'class':'form-control'}),
          'lesson_duration' : forms.TextInput(attrs={'class':'form-control'}),
          'phone_number' : forms.TextInput(attrs={'class':'form-control'}),
  
        }
