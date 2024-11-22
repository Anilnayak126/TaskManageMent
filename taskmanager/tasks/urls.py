# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("logout/", views.logout_view, name='logout'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('send_invitation/', views.send_invitation, name='send_invitation'),
    path('register/<uuid:token>/', views.register, name='register'),
]
