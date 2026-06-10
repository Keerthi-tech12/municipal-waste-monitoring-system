from django.urls import path

from .views import (
    ward_list,
    add_ward,
    edit_ward,
    delete_ward
)

urlpatterns = [

    path(
        '',
        ward_list,
        name='ward_list'
    ),

    path(
        'add/',
        add_ward,
        name='add_ward'
    ),

    path(
        'edit/<int:id>/',
        edit_ward,
        name='edit_ward'
    ),

    path(
        'delete/<int:id>/',
        delete_ward,
        name='delete_ward'
    ),

]