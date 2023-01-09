from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages as m

# Create your views here.
def login_req(req):
    if not req.user.is_authenticated:
        form = AuthenticationForm()
        if req.method == 'POST':
            data = req.POST
            form = AuthenticationForm(req, data)
            if form.is_valid():
                username = data['username']
                password = data['password']
                user = authenticate(username = username, password = password)

                if user is not None:
                    m.success(req, 'Has iniciado sesión correctamente!')
                    login(req, user)
                return redirect('index')
            else:
                m.error(req, 'Has ingresado mal los credenciales!')
                return render(req, 'user_profile/login.html', {'form': form, 'login': 1})
        else:
            return render(req, 'user_profile/login.html', {'form': form, 'login': 1})

def logout_req(req):
    if req.user.is_authenticated:
        m.info(req, 'Has cerrado sesión correctamente!')
        logout(req)
    return redirect('index')