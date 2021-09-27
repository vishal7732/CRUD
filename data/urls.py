
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("delete/<int:id>/", views.delete_data, name="delete"),
    path("<int:id>/", views.update, name="update"),
    path("edit/<int:id>/", views.single_edit, name="single_edit"),
]
