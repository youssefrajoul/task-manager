from django.urls import path

from . import views
from .views import IndexView

app_name = 'task'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('delete/<int:pk>/', views.delete_task, name='delete'),
    path('create/', views.create_task, name='create'),
]
