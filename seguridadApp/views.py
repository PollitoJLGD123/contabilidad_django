from typing import Generic
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ventasApp.forms import LoginForm,RegistroForm 
from django.contrib.auth.decorators import login_required

def ingresar_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username= user, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('homePage', username=user)  
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos") 
    else:
        form = LoginForm()
    return render(request, 'login.html', {"form": form})

def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, "Tu cuenta ha sido creada exitosamente")
            return redirect('homePage', username=usuario.username) 
        else:
            print(form.errors)
            messages.error(request, "Por favor corrige los errores")
    else:
        form = RegistroForm()
    return render(request, 'register.html', {'form': form})

@login_required
def homePage(request,username):
    context = {
        'username':username,
    }
    return render(request, "index.html", context)
def salir(request): 
    logout(request)
    messages.info(request,"Saliste exitosamente")
    return redirect("login") 