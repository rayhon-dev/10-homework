from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def home(request):
    return render(request, 'index.html')


def task_list(request):
    tasks = Task.objects.all()
    ctx = {'tasks': tasks }
    return render(request, 'tasks/task_list.html', ctx)

def task_create(request):
    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        due_date = request.POST.get('due_date')
        description = request.POST.get('description')

        if task_title and due_date and description :
            Task.objects.create(
                task_title=task_title,
                due_date=due_date,
                description=description
            )
            return redirect('tasks:task_list')
    return render(request, 'tasks/task_form.html')

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    ctx = {'task': task}
    return render(request, 'tasks/task_detail.html', ctx)

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('tasks:task_list')

def task_update(request, pk):
    task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        due_date = request.POST.get('due_date')
        description = request.POST.get('description')

        if task_title and due_date and description:
            task.task_title = task_title
            task.due_date = due_date
            task.description = description
            task.save()


            return redirect(task.get_detail_url())
    ctx ={'task': task }
    return render(request, 'tasks/task_form.html', ctx)





