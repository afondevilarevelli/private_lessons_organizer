from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.views import View


class SignUpView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'home')
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request, 'home')
        else:
            # Return an 'invalid login' error message.
            pass
