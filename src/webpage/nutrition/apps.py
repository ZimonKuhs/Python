"""
    Application configuration.

    @author:  Zimon Kuhs.
    @date:    2021-07-13.
"""

from django.apps import AppConfig


class NutritionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "nutrition"
