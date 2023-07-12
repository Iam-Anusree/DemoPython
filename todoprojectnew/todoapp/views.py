from django.shortcuts import render, redirect
from django.shortcuts import render
from . models import Task
from . forms import TodoForm
from  django.views.generic import ListView
from  django.views.generic.detail import DetailView

#from . forms import MovieForm

# Create your views here.
class TaskListview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'

class Detailview(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'task'

# Create your views here.

def add(request):
    task1= Task.objects.all()
    if request.method=='POST':
         name=request.POST.get('task','')
         priority=request.POST.get('priority','')
         date=request.POST.get('date','')
         task=Task(name=name,priority=priority,date=date)
         task.save()
    return render(request,'home.html',{'task1':task1})

def delete(request,taskid):
    if request.method=='POST':
        task = Task.objects.get(id=taskid)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task = Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})


