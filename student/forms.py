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
          'Roll_number' : forms.NumberInput(attrs={'class':'form-control'}),
          'Student_id' : forms.TextInput(attrs={'class':'form-control'}),
          'Course_name' : forms.TextInput(attrs={'class':'form-control'}),
          'country' : forms.TextInput(attrs={'class':'form-control'}),
          'age' : forms.NumberInput(attrs={'class':'form-control'}),
          'date_of_birth' : forms.DateInput(attrs={'class':'form-control'}),
          'Email_address' : forms.TextInput(attrs={'class':'form-control'}),
          'Date_of_enrollment' : forms.DateInput(attrs={'class':'form-control'}),
          'Medical_report' : forms.DateInput(attrs={'class':'form-control'}),
          'languages' : forms.TextInput(attrs={'class':'form-control'}),
          'gender' : forms.TextInput(attrs={'class':'form-control'}),

          
          
          
          
          
        }
