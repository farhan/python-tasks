from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View
from basic_auth.models import MyUser

from basic_auth.forms import LoginForm, RegisterForm
from basic_auth.messages import Message


@login_required
def home(request):
    return render(request, 'home.html')


def log_out(request):
    logout(request)
    return render(request, 'home.html')


class RegisterView(View):
    template_name = 'register.html'
    form_class = RegisterForm

    def get(self, request):
        if request.user.is_authenticated():
            return redirect(reverse('home'))
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated():
            return redirect(reverse('home'))
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request):
        if request.user.is_authenticated():
            return redirect(reverse('home'))
        form = self.form_class(
            None, initial={'email': request.GET.get('email', '')})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated():
            return redirect(reverse('home'))
        form = self.form_class(request.POST)
        message = ''
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(self.request, user)
                    return redirect(reverse('home'))
                else:
                    message = Message.LOGIN_USER_DISABLED
            else:
                message = Message.LOGIN_INVALID
        return render(self.request, self.template_name, {'error': message, 'form': form})
