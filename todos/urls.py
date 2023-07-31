from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todos_list'),
    path('<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/update/', views.TodoUpdateView.as_view(), name='todo_update'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='todo_delete'),
]
