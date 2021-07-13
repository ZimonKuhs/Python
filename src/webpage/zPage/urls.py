from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("nutrition/", include("nutrition.urls")),
    path("admin/", admin.site.urls)
]