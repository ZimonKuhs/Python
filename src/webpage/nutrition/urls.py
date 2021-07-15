"""
@author:  Zimon Kuhs.
@date:    2021-07-09.
"""

from django.urls import path
from . import views

app_name="nutrition"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("<str:person_name>/", views.person, name="person")
]