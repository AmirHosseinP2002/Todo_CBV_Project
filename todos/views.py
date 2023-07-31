from django.shortcuts import render
from django.views import generic

from .models import Todo


class TodoListView(generic.ListView):
    # model = Todo -> Todo.objects.all()
    template_name = 'todos/todos_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)
