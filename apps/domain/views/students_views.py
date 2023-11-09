from typing import Any
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from apps.domain.forms.student_forms import StudentForm
from apps.domain.models.student import Student
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.core.exceptions import PermissionDenied
from apps.domain.permissions.student_permissions import has_student_permissions


class StudentsListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'domain/students/index.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['student_form'] = StudentForm
        return ctx

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(owner=self.request.user)

    def post(self, request):
        form = StudentForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return JsonResponse(instance, status=200)
        return JsonResponse(form, status=400, safe=True)


class StudentsUpdateDestroy(LoginRequiredMixin, View):
    def put(self, request, pk):
        instance = get_object_or_404(Student, id=pk)

        if not has_student_permissions(request.user, instance):
            raise PermissionDenied()

        form = StudentForm(request.PUT or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return JsonResponse(instance, status=200)
        return JsonResponse(form, status=400)

    def delete(self, request):
        pass
