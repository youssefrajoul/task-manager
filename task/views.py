from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from task.forms import TaskForm
from task.models import Task


class IndexView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Task
    template_name = "task/index.html"
    context_object_name = 'tasks'
    permission_required = 'task.task_management'

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
