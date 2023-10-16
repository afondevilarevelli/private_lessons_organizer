from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from apps.authentication.forms.signup_form import SignUpForm


class SignUpView(View):
    form_class = SignUpForm
    initial = {'key': 'value'}
    template_name = 'authentication/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})
