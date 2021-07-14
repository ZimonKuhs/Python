"""
@author:  Zimon Kuhs.
@date:    2021-07-14.

Quick test script for creating test person and macros.
This is to facilitate synchronizing test databases across development environments.

TODO:     Remove when redundant?
"""

import django
django.setup()

from django.utils import timezone
from nutrition.models import Person, Macros

p = Person.objects.create(name = "Z", weight = 85.9, register_date = timezone.now())
m = Macros.objects.create(
            person=p,
            label = "standard",
            kCal = 3000,
            carbs = 300,
            fat = 100,
            protein = 150,
            fiber = 50,
            sugar = 50
    )

p.save()
m.save()