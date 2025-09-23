# clients/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('create/', views.client_create, name='client_create'),
    path('<int:pk>/', views.client_detail, name='client_detail'),
    path('<int:pk>/update/', views.client_update, name='client_update'),
    path('<int:pk>/delete/', views.client_delete, name='client_delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/archive/', views.task_archive, name='task_archive'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]