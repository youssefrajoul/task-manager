from django.shortcuts import render, get_object_or_404
from .models import Developer
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import DeveloperForm, ShortDeveloperForm
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, ListView):
    model = Developer
    template_name = "developer/index.html"
    context_object_name = 'developers'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = ShortDeveloperForm
        context['app'] = "developer"
        return context


class DevDetailView(LoginRequiredMixin, DetailView):
    model = Developer
    template_name = 'developer/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['app'] = "developer"
        return context


def create(request):
    form = ShortDeveloperForm(request.POST)
    if form.is_valid():
        Developer.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            username=form.cleaned_data['username'],
        )
    # Toujours renvoyer une HTTPResponseRedirect après avoir géré correctement
    # les données de la requête POST. Cela empêche les données d'être postée deux
    # fois si l'utilisateur clique sur le bouton précédent.
    return HttpResponseRedirect(reverse('developer:index'))


def delete(request, pk):
    obj = Developer.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('developer:index'))
