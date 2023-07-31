from django.shortcuts import render, reverse
from django.views import generic
from django.urls import reverse_lazy

from .models import Todo
from .forms import TodoForm


class TodoListView(generic.ListView):
    # model = Todo -> Todo.objects.all()
    template_name = 'todos/todos_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)


class TodoDetailView(generic.DetailView):
    model = Todo
    template_name = 'todos/todo_detail.html'
    context_object_name = 'todo'


class TodoCreateView(generic.CreateView):
    form_class = TodoForm
    template_name = 'todos/todo_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todos:todos_list')


class TodoUpdateView(generic.UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_update.html'

    def get_success_url(self):
        return reverse('todos:todo_detail', args=[self.object.id])


class TodoDeleteView(generic.DeleteView):
    model = Todo
    template_name = 'todos/todo_delete.html'
    success_url = reverse_lazy('todos:todos_list')
