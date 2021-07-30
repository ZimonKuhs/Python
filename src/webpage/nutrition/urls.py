"""
    URL direction for the nutrition application.

    @author:  Zimon Kuhs.
    @date:    2021-07-09.
"""

from django.urls import path

from . import views

app_name="nutrition"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("registerNew/", views.registerNew, name="registerNew"),
    path("<str:personName>/", views.person, name="person")
]
