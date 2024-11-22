# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.mail import send_mail
from .models import Task, Invitation
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            Task.objects.create(user=request.user, title=title, description=description)
            return redirect(reverse('task_list'))
        else:
            error = 'Please correct the errors below.'
            return render(request, 'task_form.html', {'error': error})

    return render(request, 'task_form.html')

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            task.title = title
            task.description = description
            task.save()
            return redirect(reverse('task_list'))
        else:
            error = 'Please correct the errors below.'
            return render(request, 'task_form.html', {'task': task, 'error': error})

    return render(request, 'task_form.html', {'task': task})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('task_list'))
    return render(request, 'task_confirm_delete.html', {'task': task})

@login_required
def send_invitation(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            invitation = Invitation.objects.create(email=email, invited_by=request.user)
            send_invitation_email(invitation.email, invitation.token)
            return redirect(reverse('home'))
        else:
            error = 'Please enter a valid email address.'
            return render(request, 'send_invitation.html', {'error': error})
    return render(request, 'send_invitation.html')

def send_invitation_email(email, token):
    subject = 'You are invited to join our Task Management App'
    message = f'Please click the link to register: {settings.SITE_URL}/register/{token}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

def register(request, token):
    invitation = get_object_or_404(Invitation, token=token, is_used=False)
    if request.user.is_authenticated:
        invitation.is_used = True
        invitation.save()
        return redirect(reverse('home'))
    return render(request, 'google_login.html', {'token': token})
