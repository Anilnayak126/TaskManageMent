from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Task
from .forms import TaskForm  

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
