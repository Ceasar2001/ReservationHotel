from django.urls import path
from .views import (
    reservation_list,
    reservation_create,
    reservation_redirect,
    reservation_update,
    reservation_delete,
)

urlpatterns = [
    path('', reservation_redirect, name='reservation_redirect'),  # Redirect to reservation list
    path('list/', reservation_list, name='reservation_list'),
    path('create/', reservation_create, name='reservation_create'),
    path('update/<int:pk>/', reservation_update, name='reservation_update'),
    path('delete/<int:pk>/', reservation_delete, name='reservation_delete'),
]