from django.contrib.gis.db import models


class Tracking(models.Model):
    position = models.PointField()
    houmer = models.ForeignKey('houmer', on_delete=models.CASCADE,
        related_name='trackings')
    timestamp = models.DateTimeField(auto_now_add=True)


class Houmer(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.name)


class Property(models.Model):
    location = models.PointField()
    description = models.TextField(blank=True, null=True)
