from django.contrib import admin
from django.urls import include, path
import apps.domain.views.home_views as home_views

urlpatterns = [
    path("", home_views.home, name='home'),
    path("dashboard", home_views.dashboard, name='dashboard'),
]
