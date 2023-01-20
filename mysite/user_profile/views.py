from django.shortcuts import render, redirect
from .forms import NewAuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages as m
from django.views.decorators.csrf import requires_csrf_token

# Create your views here.
@requires_csrf_token
def login_req(req):
    if not req.user.is_authenticated:
        form = NewAuthenticationForm()
        if req.method == 'POST':
            data = req.POST
            form = NewAuthenticationForm(req, data)
            if form.is_valid():
                username = data['username']
                password = data['password']
                user = authenticate(username = username, password = password)

                if user is not None:
                    m.success(req, 'Has iniciado sesión correctamente!')
                    login(req, user)
                return redirect('main:index')
            else:
                m.error(req, 'Has ingresado mal los credenciales!')
                return render(req, 'user_profile/login.html', {'form': form, 'login': 1})
        else:
            return render(req, 'user_profile/login.html', {'form': form, 'login': 1})

@login_required
def logout_req(req):
    m.info(req, 'Has cerrado sesión correctamente!')
    logout(req)
    return redirect('main:index')