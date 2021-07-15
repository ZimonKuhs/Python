"""
@author:  Zimon Kuhs.
@date:    2021-07-09.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("nutrition.urls")),
    path("nutrition/", include("nutrition.urls")),
]