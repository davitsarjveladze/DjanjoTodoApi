from django.urls import path
from . import views


urlpatterns = [
    path('getall', views.todos),
    path('insert', views.insert),
    path('update', views.update),
    path('delete', views.delete)
]