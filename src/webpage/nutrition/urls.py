"""
@author:  Zimon Kuhs.
@date:    2021-07-09.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.nutrition, name="nutrition"),
    path("<str:person_name>/", views.person, name="person")
]