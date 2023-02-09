from django.urls import path

from . import views

urlpatterns = [
    path('table/', views.get_table, name='get_table'),
    path("form/", views.get_form, name="get_form"),
    path('new/', views.create_request, name='create_request'),
    path('edit=<str:id>/', views.edit_request, name='edit_request'),
    path('delete/id=<int:id>/', views.delete_request, name='delete_request'),

]