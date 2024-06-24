from django.shortcuts import render, get_object_or_404
from .models import Developer


def index(request):
    context = {
        'developers': Developer.objects.all()
    }

    return render(request, 'developer/index.html', context)


def detail(request, developer_id):
    developer = get_object_or_404(Developer, pk=developer_id)
    return render(request, 'developer/detail.html', {'developer': developer})
