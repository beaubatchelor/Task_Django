from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('organizations/', views.organizations),
    path('values/', views.values),
    path('tasks/', views.tasks),
]