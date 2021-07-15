from django.http import JsonResponse
from django.core import serializers

from .models import Todos


# Create your views here.
def todos(request):
    return JsonResponse({'status': 1,
                         'data': serializers.serialize("json", Todos.objects.all())})


def insert(request):
    todo = Todos(title=request.GET['title'])
    todo.save()
    if todo.id:
        return JsonResponse({'status': 1, 'id': todo.id})
    return JsonResponse({'status': 0})


def update(request):
    todo = Todos(title=request.GET['title'],
                 status=request.GET['status'],
                 id=request.GET['id'])
    todo.save()
    if todo.id:
        return JsonResponse({'status': 1})
    return JsonResponse({'status': 0})
