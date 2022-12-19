import django
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import *
from .services import create_user, auth_user


class UserRegisterView(FormView):
    template_name = 'authentication/register.html'
    success_url = "/login"
    form_class = UserRegistrationForm

    def post(self, request, *args, **kwargs):
        try:
            create_user(request)
            return redirect('login')
        except django.db.utils.IntegrityError:
            messages.info(request, 'Пользователь с такой почтой уже существует')
            return redirect('registration')


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('profile')
    form_class = UserLoginForm

    def post(self, request, *args, **kwargs):
        user = auth_user(request)
        if user is not None:
            login(request, user)
            return redirect('/profile')
        messages.error(request, "Пользователя с такими данными не существует")
        return redirect('login')

    def get(self, request, *args, **kwargs):
        return render(request, 'authentication/login.html', {'form': UserLoginForm})


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')
