from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from apps.authentication.forms.login_form import LoginForm
from apps.authentication.forms.reset_password_form import ResetPasswordForm
from apps.authentication.views import SignUpView

urlpatterns = [
    path("signup", SignUpView.as_view(), name='signup'),

    path("login/", auth_views.LoginView.as_view(
        template_name='authentication/login.html', form_class=LoginForm), name='login'),

    path("logout/", auth_views.LogoutView.as_view(), name='logout'),

    path("change-password/", auth_views.PasswordChangeView.as_view()),

    path("change-password/done/", auth_views.PasswordChangeDoneView.as_view()),

    path("reset-password/", auth_views.PasswordResetView.as_view(
        template_name='authentication/password_reset.html', form_class=ResetPasswordForm
    ), name='password_reset'),

    path("reset-password/done/", auth_views.PasswordResetDoneView.as_view(
        template_name='authentication/password_reset_done.html'
    ), name='password_reset_done'),

    path("reset/done/", auth_views.PasswordResetCompleteView.as_view()),

    path("reset/<str:uidb64>/<str:token>/",
         auth_views.PasswordResetConfirmView.as_view()),
]
