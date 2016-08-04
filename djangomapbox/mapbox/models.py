from django.contrib.gis.db import models


class MDoutpoint(models.Model):
    name = models.CharField(max_length=6)
    lon = models.FloatField()
    lat = models.FloatField()
    points = models.PointField()

    def __str__(self):
        return self.name

class outpointMD(models.Model):
    경도 = models.FloatField()
    위도 = models.FloatField()
    이름 = models.CharField(max_length=6)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return self.이름
