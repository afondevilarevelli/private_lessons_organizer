from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    messages.info(request, f'asd created for')
    messages.warning(request, f'Account created for')
    messages.error(request, f'Account created for')
    return render(request, 'home.html')


@login_required
def dashboard(request):
    return render(request, 'domain/dashboard.html')
