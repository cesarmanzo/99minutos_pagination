from django.db import models


class Orders(models.Model):
    fecha = models.DateTimeField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    repartidor = models.CharField(max_length=200, blank=True, null=True)