"""
@author:  Zimon Kuhs.
@date:    2021-07-09.
"""

from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="fallBack"),
    path("nutrition/", include("nutrition.urls")),
    path("admin/", admin.site.urls)
]