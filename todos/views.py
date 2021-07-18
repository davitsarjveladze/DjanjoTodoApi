from django.http import JsonResponse
from django.core import serializers
import json

from .models import Todos


def todos(request):
    return_array = list()
    todolist = Todos.objects.all()
    for todo in todolist:
        item = {'id': todo.pk,
                'title': todo.title,
                'status': todo.status,
                'order': todo.order}

        return_array.append(item)

    return JsonResponse({'status': 1,
                         'data': return_array})


def insert(request):
    todo = Todos(title=request.GET['title'], order=request.GET['order'])
    todo.save()
    if todo.id:
        return JsonResponse({'status': 1, 'id': todo.id})
    return JsonResponse({'status': 0})


def update(request):
    todo = Todos(title=request.GET['title'],
                 status=request.GET['status'],
                 id=request.GET['id'],
                 order=request.GET['order'])
    todo.save()
    if todo.id:
        return JsonResponse({'status': 1})
    return JsonResponse({'status': 0})


def delete(request):
    data = json.loads(request.GET['ides'])
    result = Todos.objects.filter(pk__in=data).delete()
    if result[0] > 0:
        return JsonResponse({'status': 1})
    return JsonResponse({'status': 0})
