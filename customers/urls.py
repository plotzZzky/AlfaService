from django.urls import path

from . import views


urlpatterns = [
    path("table/", views.get_table, name="get_customers_table"),
    path("form/", views.get_form, name="get_form"),
    path("new/", views.create_customer, name="new_customer"),
    path("edit=<int:id>/", views.edit_customer, name="edit_customer"),
    path("delete/id=<int:id>/", views.delete_customer, name="delete_customer"),
]