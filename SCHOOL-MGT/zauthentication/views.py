from django.shortcuts import render, redirect
from users.forms import CustomUserCreationForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form':form})


def logoutt(request):
    return render(request, 'registration/logoutt.html', {})