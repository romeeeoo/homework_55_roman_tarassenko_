from django.shortcuts import render, redirect, get_object_or_404
from todo_app.models import Task


# Create your views here.
def index_view(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def add_view(request):
    if request.method == 'GET':
        return render(request, 'add_new_task.html')
    elif request.method == 'POST':
        description = request.POST.get('description'),
        status = request.POST.get('status'),
        deadline = request.POST.get('deadline')
        new_task = Task.objects.create(description=description[0], status=status[0],
                                       deadline=deadline)
        new_task.save()
        return redirect("index_view")


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'detailed_task.html', context={'task': task})


