from django.contrib.gis.db import models


class Tracking(models.Model):
    position = models.PointField()
    houmer = models.ForeignKey('houmer', on_delete=models.CASCADE,
                               related_name='trackings')
    timestamp = models.DateTimeField(auto_now_add=True)
    velocity = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Tracking"
        ordering = ("-timestamp", )

    def __str__(self):
        return 'Track {} - Houmer {}'.format(self.id, self.houmer)


class Houmer(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.name)


class Property(models.Model):
    polygon = models.PolygonField()
    description = models.TextField(blank=True, null=True)
