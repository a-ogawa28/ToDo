from django.urls import path
from . import views


app_name = 'todo'
urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('list/', views.TodoList.as_view(), name='todo_list'),
    path('status/', views.TodoStatus.as_view(), name='todo_status'),
    path('detail/<int:pk>/', views.TodoDetail.as_view(), name='todo_detail'),
    path('create/', views.TodoCreate.as_view(), name='todo_create'),
    path('update/<int:pk>/', views.TodoUpdate.as_view(), name='todo_update'),
    path('delete/<int:pk>/', views.TodoDelete.as_view(), name='todo_delete'),
    path('reply/<int:pk>/', views.ReplyCreate.as_view(), name='reply_create'),

]
