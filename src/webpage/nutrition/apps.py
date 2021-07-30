"""
    Application configuration.

    @author:  Zimon Kuhs.
    @date:    2021-07-13.
"""

from django.apps import AppConfig

"""
    Nutrition application configuration.

    N.B. Purpose currently unclear to the author.
"""
class NutritionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "nutrition"
