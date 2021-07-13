"""
@author:  Zimon Kuhs.
@date:    2021-07-13.
"""

from django.contrib import admin

from .models import Question

admin.site.register(Question)