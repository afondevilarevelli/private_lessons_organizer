from django.http import HttpResponse
from django.views.generic import ListView
from apps.domain.models.student import Student
from django.contrib.auth.mixins import LoginRequiredMixin


class StudentsListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'domain/students/index.html'
    context_object_name = 'students'
