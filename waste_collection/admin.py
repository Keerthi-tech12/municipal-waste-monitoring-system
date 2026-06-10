from django.contrib import admin
from .models import WasteCollection

@admin.register(WasteCollection)
class WasteCollectionAdmin(admin.ModelAdmin):
    list_display = (
        'collection_date',
        'collection_time',
        'ward',
        'vehicle',
        'loaded_weight',
        'empty_weight',
        'waste_quantity',
    )

    list_filter = (
        'collection_date',
        'ward',
    )

    search_fields = (
        'ward__ward_name',
        'vehicle__vehicle_number',
    )