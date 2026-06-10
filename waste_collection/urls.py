from django.urls import path
from .views import (
    add_waste_collection,
    collection_history,
    edit_collection,
    delete_collection
)

urlpatterns = [

    path(
        '',
        add_waste_collection,
        name='add_waste_collection'
    ),

    path(
        'history/',
        collection_history,
        name='collection_history'
    ),

    path(
        'edit/<int:id>/',
        edit_collection,
        name='edit_collection'
    ),

    path(
        'delete/<int:id>/',
        delete_collection,
        name='delete_collection'
    ),

]