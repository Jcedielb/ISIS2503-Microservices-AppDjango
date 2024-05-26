from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=255, null=False, default=None)

    def __str__(self):
        return self.name

class Measurement(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
