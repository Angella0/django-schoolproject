from django import forms
from django.forms import ModelForm, widgets
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = "__all__"
        widgets ={
          'first_name' : forms.TextInput(attrs={'class':'form-control'}),
          'last_name' : forms.TextInput(attrs={'class':'form-control'}),
          'roll_number' : forms.NumberInput(attrs={'class':'form-control'}),
          'student_id' : forms.TextInput(attrs={'class':'form-control'}),
          'course_name' : forms.TextInput(attrs={'class':'form-control'}),
          'age' : forms.NumberInput(attrs={'class':'form-control'}),
          'date_of_birth' : forms.DateInput(attrs={'class':'form-control'}),
          'email_address' : forms.TextInput(attrs={'class':'form-control'}),
          'date_of_enrollment' : forms.DateInput(attrs={'class':'form-control'}),
          'medical_report' : forms.FileInput(attrs={'class':'form-control'}),
          
          
          
          
          
          
        }
