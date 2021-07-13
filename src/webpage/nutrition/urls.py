from django.urls import path
from . import views

urlpatterns = [
    path("", views.nutrition, name="nutrition"),
    path("data/", views.data, name="data")
]