"""
@author:  Zimon Kuhs.
@date:    2021-07-13.
"""

import datetime

from django.db.models import CASCADE, Model, ForeignKey, CharField, DateTimeField, DecimalField, IntegerField
from django.utils import timezone

class Person(Model):
    def __str__(self):
        return self.name

    name = CharField(max_length = 100)
    register_date = DateTimeField("Date registered.")
    weight = DecimalField(decimal_places = 3, max_digits = 7)

class Macros(Model):
    """
        Represents the recommended macronutrient intake for a person.

        Attributes:
            label(str):     Label to signify a version of recommendations.
            kCal(float):    Recommended calories.
            carbs(float):   Recommended carbs.
            fat(float):     Recommended fat.
            protein(float): Recommended protein.
            fiber(float):   Recommended fiber.
            sugar(float):   Recommended sugar.

        TODO: This data structure can be represented less hamfistedly.
              Using lists and/or dictionaries.
    """
    def __str__(self):
        return str({
            "label": self.label,
            "kCal": self.kCal,
            "carbs": self.carbs,
            "fat": self.fat,
            "protein": self.protein,
            "fiber": self.fiber,
            "sugar": self.sugar
        })

    person = ForeignKey(Person, on_delete = CASCADE)

    label = CharField(max_length = 100)
    kCal = DecimalField   (decimal_places = 3, max_digits = 8)
    carbs = DecimalField  (decimal_places = 3, max_digits = 8)
    fat = DecimalField    (decimal_places = 3, max_digits = 8)
    protein = DecimalField(decimal_places = 3, max_digits = 8)
    fiber = DecimalField  (decimal_places = 3, max_digits = 8)
    sugar = DecimalField  (decimal_places = 3, max_digits = 8)

    def values(self):
        return {
            "label": self.label,
            "kCal": self.kCal,
            "carbs": self.carbs,
            "fat": self.fat,
            "protein": self.protein,
            "fiber": self.fiber,
            "sugar": self.sugar
        }

class Question(Model):

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

    question_text = CharField(max_length = 200)
    pub_date = DateTimeField("date published")

class Choice(Model):
    def __str__(self):
        return self.choice_text

    question = ForeignKey(Question, on_delete = CASCADE)
    choice_text = CharField(max_length = 200)
    votes = IntegerField(default = 0)