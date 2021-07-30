"""
    General URL direction.

    @author:  Zimon Kuhs.
    @date:    2021-07-09.
"""

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.gotoIndex),
    path("index/", views.index),
    path("nutrition/", include("nutrition.urls")),
]
