# instructors/forms.py
from django import forms
from .models import InstructorProfile

class InstructorProfileForm(forms.ModelForm):
    class Meta:
        model = InstructorProfile
        fields = ['bio', 'profile_picture', 'qualifications', 'experience', 'social_links']
        widgets = {
            'bio': forms.Textarea(attrs={'placeholder': 'Tell us about yourself'}),
            'profile_picture': forms.ClearableFileInput(),
            'qualifications': forms.Textarea(attrs={'placeholder': 'Your qualifications'}),
            'experience': forms.NumberInput(attrs={'placeholder': 'Years of experience'}),
            'social_links': forms.TextInput(attrs={'placeholder': 'Social media links in JSON format'}),
        }
