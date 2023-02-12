from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("create_info/", views.create_info, name="create_info"),
]
