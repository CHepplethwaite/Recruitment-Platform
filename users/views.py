from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

#user registration views

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, {username}! You are now able to log in.')
            return redirect('log_in')
    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})
