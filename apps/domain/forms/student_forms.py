from typing import Any
from django.forms import ModelForm
from apps.domain.models.student import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "contact_email", "image"]
