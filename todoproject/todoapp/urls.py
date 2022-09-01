from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    # path('', views.home, name='home'),
    # # path('details/', views.details, name='details'),
    # path('delete/<int:task_id>', views.delete, name='delete'),
    # path('update/<int:task_id>', views.update_task, name='update_task'),
    path('listview/', views.TaskListView.as_view(), name='TaskListView'),
    path('detailview/<int:pk>/', views.TaskDetailView.as_view(), name='TaskDetailView'),
    path('updateview/<int:pk>', views.TaskUpdateView.as_view(), name='TaskUpdateView'),
    path('deleteview/<int:pk>', views.TaskDeleteView.as_view(), name='TaskDeleteView'),


]