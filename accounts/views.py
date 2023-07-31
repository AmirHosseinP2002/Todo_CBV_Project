from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authentication successfully')
                else:
                    return HttpResponse('Disable Login')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {
        'form': form
    })


def logout_view(request):
    logout(request)
    return HttpResponse('Logout successfully')
