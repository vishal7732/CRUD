from django.core import validators
from django import forms
from .models import Student

# To Update all fields
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Name', 'email', 'Roll_No']


# To Update single fields
class StudentRegistration1(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Roll_No']