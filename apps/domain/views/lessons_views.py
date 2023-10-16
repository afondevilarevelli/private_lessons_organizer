from django.http import HttpResponse
from django.views.generic import ListView
from apps.domain.models.lesson import Lesson
from django.contrib.auth.mixins import LoginRequiredMixin


class LessonsListView(LoginRequiredMixin, ListView):
    model = Lesson
    template_name = 'domain/lessons/index.html'
    context_object_name = 'lessons'
