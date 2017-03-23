from django.shortcuts import render, redirect, HttpResponse
from models import Task

# Create your views here.
def showTaskView(request):
    tasks = Task.objects.all()
    return render(request, 'show_tasks.html', {'tasks' : tasks})
    
def submitTask(request):
    if request.method == "POST":
        text = request.POST.get('text', '')
        task = Task(text=text)
        task.save()
    return redirect('/showtask')