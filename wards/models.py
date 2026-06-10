from django.db import models
from zones.models import Zone

class Ward(models.Model):
    ward_name = models.CharField(max_length=100)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return self.ward_name