from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_view, name='todo_view'),
]
