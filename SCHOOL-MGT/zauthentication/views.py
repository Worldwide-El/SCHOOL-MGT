from django.shortcuts import render, redirect
from users.forms import CustomUserCreationForm

from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.is_active = False
            save_it.save()

        

            subject = 'Welcome to Moladh Institute! We pride in your excellence'
            message = 'We have received your registration request, click on the link to confirm your status!'
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.email,]

            send_mail(subject, message, from_email, to_list, fail_silently=False)

            messages.success(request, 'Thank you for signing up for Moladh Institute! \n A confirmation link has been sent to your email address')
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form':form})


def logoutt(request):
    return render(request, 'registration/logoutt.html', {})