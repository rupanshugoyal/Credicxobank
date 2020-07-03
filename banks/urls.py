"""
banks app url configuration
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loaddataset/', views.load_dataset, name='dataset'),
]