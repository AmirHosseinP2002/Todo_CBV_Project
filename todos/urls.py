from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todos_list'),
]
