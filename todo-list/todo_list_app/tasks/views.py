from django.shortcuts import render, redirect
from .models import Task
# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html',{'tasks':tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request,'tasks/task_create.html')
