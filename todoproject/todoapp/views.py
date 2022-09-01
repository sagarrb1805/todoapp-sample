from django.shortcuts import render, redirect
from .models import Task
from . froms import TaskForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    template_name ='home.html'
    context_object_name = 'tasks'

    def post(self, request):
        name = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect('todoapp:TaskListView')
class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'updateview.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todoapp:TaskDetailView', kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:TaskListView')




# def home(request):
#     tasks = Task.objects.all()
#     if request.method == 'POST':
#         name = request.POST.get('task')
#         priority = request.POST.get('priority')
#         date = request.POST.get('date')
#         task = Task(name=name, priority=priority, date=date)
#         task.save()
#         return redirect('/')

#     return render(request, 'home.html', {'tasks': tasks})



# def delete(request, task_id):
#     task = Task.objects.get(id=task_id)
#     if request.method == 'POST':
#         task.delete()
#         return redirect('/')
#     return render(request, 'delete.html')

# def update_task(request, task_id):
#     task = Task.objects.get(id=task_id)

#     form = TaskForm(request.POST or None, instance=task)
#     if form.is_valid():
#         form.save()
#         return redirect('/')

#     return render (request, 'update.html', {'task': task, 'form': form})






# def update_task(request, task_id):
#     task = Task.objects.get(id=task_id)

#     if request.method == "POST":
#         name = request.POST.get('task', '')
#         priority = request.POST.get('priority', '')
#         date = request.POST.get('date', '')
#         task.name = name
#         task.priority = priority
#         task.date = date
#         task.save()
#         return redirect('/')
#     return render(request, 'update.html', {'task': task})


