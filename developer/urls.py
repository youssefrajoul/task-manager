from django.urls import path

from . import views

app_name = 'developer'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:developer_id>/', views.detail, name='detail'),
]