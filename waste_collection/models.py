from django.db import models
from wards.models import Ward
from vehicles.models import Vehicle


class WasteCollection(models.Model):
    collection_date = models.DateField()
    collection_time = models.TimeField()

    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    loaded_weight = models.DecimalField(max_digits=10, decimal_places=2)
    empty_weight = models.DecimalField(max_digits=10, decimal_places=2)

    waste_quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False
    )

    def save(self, *args, **kwargs):
        self.waste_quantity = self.loaded_weight - self.empty_weight
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.collection_date} - {self.ward}"