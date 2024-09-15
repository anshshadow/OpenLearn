# students/forms.py

from django import forms
from .models import StudentProfile

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['address', 'bio', 'profile_picture']  # Include fields as needed
