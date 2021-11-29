from django.contrib import messages
from django.shortcuts import render, redirect

from ticket import views
from .forms import LoginForm

# Create your views here.

def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            views.fetchTickets(form.cleaned_data['username'], form.cleaned_data['subdomain'], form.cleaned_data['password'])
            
            if views.auth:
                return redirect('/home/')
            else:
                messages.warning(request, 'Incorrect Credentials')
                return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'title' : 'login', 'form' : form})

def logout(request):
    views.auth = False

    return render(request, 'user/logout.html', {'title' : 'logout'})