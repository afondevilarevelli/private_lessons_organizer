from django import forms
from django.forms import ModelForm
from apps.domain.models.student import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "contact_email", "image"]
        widgets = {
            'first_name': forms.TextInput(
                attrs={"autofocus": True, 'class': 'mb-2 form-control'}),
            'last_name': forms.TextInput(
                attrs={'class': 'mb-2 form-control'}),
            'contact_email': forms.EmailInput(
                attrs={'class': 'mb-2 form-control'}),
            'image': forms.FileInput(
                attrs={'class': 'mb-2 form-control'})
        }
