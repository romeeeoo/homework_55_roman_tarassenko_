from django.shortcuts import render, redirect, get_object_or_404

from todo_app.forms import TaskForm
from todo_app.models import Task


# Create your views here.
def index_view(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def add_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'add_new_task.html', context={'form': form})
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = Task.objects.create(
                description=form.cleaned_data['description'],
                detailed_description=form.cleaned_data['detailed_description'],
                status=form.cleaned_data['status'],
                deadline=form.cleaned_data['deadline']
            )
            return redirect("detailed_task", pk=new_task.pk)
        else:
            return render(request, 'add_new_task.html', context={'form': form})


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'detailed_task.html', context={'task': task})


def update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.detailed_description = form.cleaned_data['detailed_description']
            task.status = form.cleaned_data['status']
            task.deadline = form.cleaned_data['deadline']
            task.save()
            return redirect('detailed_task', pk=task.pk)
    elif request.method == 'GET':
        form = TaskForm(initial={
            'description': task.description,
            'detailed_description': task.detailed_description,
            'status': task.status,
            'deadline': task.deadline
        })
        return render(request, 'update_task.html', context={'task': task, 'form': form})


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_confirm_delete.html', context={'task': task})


def confirm_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')
