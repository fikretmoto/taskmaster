from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.
def index(request):
  
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
                form.save()
        
        return redirect('/')     

    else:
         form=TaskForm()
      
   
   
    tasks =Task.objects.all()

    context={
        'tasks':tasks,
        'form':form
    }

    return render(request, 'task/index.html', context)

def mark_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_done = True
    task.save()
    return redirect('/')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')