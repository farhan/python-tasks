import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import View

from basic_auth.forms import LoginForm, RegisterForm
from basic_auth.messages import Message


def log_out(request):
    logout(request)
    return render(request, 'home.html')


class BaseView(View):
    def get(self, request):
        if request.GET.get('logout'):
            return redirect(reverse('logout'))


class HomeView(BaseView):
    template_name = 'home.html'

    def get(self, request):
        if not request.GET:
            return render(request, self.template_name)
        return super(HomeView, self).get(request)


class RegisterView(BaseView):
    template_name = 'register.html'
    form_class = RegisterForm

    def get(self, request):
        if request.user.is_authenticated():
            return redirect(reverse('home'))
        if not request.GET:
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


class LoginView(BaseView):
    # Following are not overridden fields but new fields define in the class
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request):
        if request.user.is_authenticated():
            return redirect(reverse('home'))
        if not request.GET:
            form = LoginForm(None, initial={'email': request.GET.get('email', '')})
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


def current_datetime(request):
    """
    View: A view function, or view for short, is a Python function that takes a Web request and returns a Web response.
    An example of simple view returning the current date time
    """
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
