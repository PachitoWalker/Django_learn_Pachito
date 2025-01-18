from django.shortcuts import render

# Create your views here.

def login(request):
    context = {
        'title':'Home - вход'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title':'Home - регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title':'Home - профиль'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...