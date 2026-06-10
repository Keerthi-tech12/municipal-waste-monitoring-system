from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path(
    'vehicles/',
    include('vehicles.urls')
    ),

    path(
    'wards/',
    include('wards.urls')
    ),
    

    path(
    'zones/',
    include('zones.urls')
    ),

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        include('dashboard.urls')
    ),

    path(
        'reports/',
        include('reports.urls')
    ),

    path(
        'waste-collection/',
        include('waste_collection.urls')
    ),

    path(
        '',
        include('users.urls')
    ),

]