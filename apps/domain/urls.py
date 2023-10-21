from django.contrib import admin
from django.urls import include, path
import apps.domain.views.home_views as home_views
from apps.domain.views.lessons_views import LessonsListView
from apps.domain.views.students_views import StudentsListView

urlpatterns = [
    path("", home_views.home, name='home'),
    path("dashboard", home_views.dashboard, name='dashboard'),
    path("students", StudentsListView.as_view(), name='students_list'),
    path("lessons", LessonsListView.as_view(), name='lessons_list'),
]
