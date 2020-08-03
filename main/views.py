from django.shortcuts import render
from main.forms import RegisterUserForm
from main.forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        login_user_form = LoginUserForm(data=request.POST)
        if login_user_form.is_valid():
            user = authenticate(login_user_form)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponse("Your account was inactive.")
            else:
                return HttpResponse("Invalid login details given")
    else:
        login_form = LoginUserForm()
        return render(request, 'login.html', {
            'form': login_form
        })

def register(request):
    if request.method == 'POST':
        register_user_form = RegisterUserForm(data=request.POST)
        if register_user_form.is_valid():
            user = register_user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse("no")
    else:
        register_form = RegisterUserForm()
        return render(request, 'register.html', {
            'form': register_form
        })