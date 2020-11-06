from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['email'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("accounts:dashboard")
                else:
                    return HttpResponse("User account is disabled")
            else:
                return HttpResponse("Invalid User")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required()
def user_dashboard(request):
    return render(request, 'account/dashboard.html')
