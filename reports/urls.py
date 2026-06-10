from django.urls import path
from .views import (
    daily_report,
    ward_report,
    zone_report,
    monthly_report,
    export_ward_excel,
    export_ward_pdf
)

urlpatterns = [
    path('daily/', daily_report, name='daily_report'),
    path('ward/', ward_report, name='ward_report'),
    path('zone/', zone_report, name='zone_report'),
    path('monthly/', monthly_report, name='monthly_report'),

    path(
        'ward/export-excel/',
        export_ward_excel,
        name='export_ward_excel'
    ),
    path(
    'ward/export-pdf/',
    export_ward_pdf,
    name='export_ward_pdf'
),
]