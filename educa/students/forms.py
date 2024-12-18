from django import forms

from courses.models import Course
from .models import StudentWork


class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.none(),
        widget=forms.HiddenInput
    )

    def __init__(self, *args, **kwargs):
        super(CourseEnrollForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.all()

class StudentWorkForm(forms.ModelForm):
    class Meta:
        model = StudentWork
        fields =['title','content','image','video','file','link']
        widgets = {
            'image':forms.ClearableFileInput(attrs={'accept':'image/png'}),
            'video':forms.ClearableFileInput(attrs={'accept': 'video/mp4'}),
            'file': forms.ClearableFileInput(attrs={'accept':'application/pdf'}),
        }