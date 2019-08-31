from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Marker(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=False, blank=False, default='No description given')
    longitude = models.DecimalField(decimal_places=20, max_digits=25, null=True, blank=True)
    latitude = models.DecimalField(decimal_places=20, max_digits=25, null=True, blank=True)
    marker_region = models.ForeignKey(Region, on_delete=models.CASCADE)
