from django.db import models


# Create your models here.
class Todos(models.Model):
    title = models.TextField()
    status = models.BooleanField(default=0)
    order = models.FloatField(default=0)
