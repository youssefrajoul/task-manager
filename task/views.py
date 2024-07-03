from django.shortcuts import render

from task.forms import TaskForm
from task.models import Task
from django.views.generic import DetailView, ListView
from django.http import HttpResponseRedirect
from django.urls import reverse


class IndexView(ListView):
    model = Task
    template_name = "task/index.html"
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = TaskForm
        context['app'] = "task"
        return context


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return HttpResponseRedirect(reverse('task:index'))


def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        Task.objects.create(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            assignee=form.cleaned_data['assignee'],
        )
    return HttpResponseRedirect(reverse('task:index'))
