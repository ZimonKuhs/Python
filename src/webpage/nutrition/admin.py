"""
@author:  Zimon Kuhs.
@date:    2021-07-13.
"""

from django.contrib import admin

from .models import Person, Macros

admin.site.register(Person)
admin.site.register(Macros)