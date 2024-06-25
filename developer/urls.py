from django.urls import path

from . import views
from .views import DevDetailView, IndexView

app_name = 'developer'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DevDetailView.as_view(), name='detail'),
    path('create/', views.create, name='create'),
]
