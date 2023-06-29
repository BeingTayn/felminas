from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
@login_required()


def principal(request):
    titulo="Inicio"
    context={
        "titulo":titulo
    }
    return render(request, "index.html",context)

def logout_user(request):
    logout(request)
    return redirect('inicio')
