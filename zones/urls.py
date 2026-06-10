from django.urls import path

from .views import (
    zone_list,
    add_zone,
    edit_zone,
    delete_zone
)

urlpatterns = [

    path(
        '',
        zone_list,
        name='zone_list'
    ),

    path(
        'add/',
        add_zone,
        name='add_zone'
    ),

    path(
        'edit/<int:id>/',
        edit_zone,
        name='edit_zone'
    ),

    path(
        'delete/<int:id>/',
        delete_zone,
        name='delete_zone'
    ),

]