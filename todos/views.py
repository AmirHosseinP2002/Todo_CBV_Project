from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Todo
from .forms import TodoForm


class TodoListView(LoginRequiredMixin, generic.ListView):
    # model = Todo -> Todo.objects.all()
    template_name = 'todos/todos_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)


class TodoDetailView(LoginRequiredMixin, generic.DetailView):
    model = Todo
    template_name = 'todos/todo_detail.html'
    context_object_name = 'todo'


class TodoCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = TodoForm
    template_name = 'todos/todo_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todos:todos_list')


class TodoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_update.html'

    def get_success_url(self):
        return reverse('todos:todo_detail', args=[self.object.id])


class TodoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Todo
    template_name = 'todos/todo_delete.html'
    success_url = reverse_lazy('todos:todos_list')


class TodoUpdateCheckboxView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        todo = get_object_or_404(Todo, pk=pk)
        is_completed = self.request.POST.get('is_completed', False) == 'on'
        todo.is_completed = is_completed
        todo.save()
        return redirect('todos:todos_list')


class TodoDeleteIconView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return redirect('todos:todos_list')
