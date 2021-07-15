"""
@author:  Zimon Kuhs.
@date:    2021-07-13.
"""

from django.db.models import CASCADE, Model, ForeignKey, CharField, DateTimeField, DecimalField

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
            person(Person): The owner of the macros.
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
    person = ForeignKey(Person, on_delete = CASCADE)

    label = CharField(max_length = 100)
    kCal = DecimalField(decimal_places = 2, max_digits = 8)
    carbs = DecimalField(decimal_places = 2, max_digits = 8)
    fat = DecimalField(decimal_places = 2, max_digits = 8)
    protein = DecimalField(decimal_places = 2, max_digits = 8)
    fiber = DecimalField(decimal_places = 2, max_digits = 8)
    sugar = DecimalField(decimal_places = 2, max_digits = 8)

    @classmethod
    def auto(cls, weight):
        label = "auto"
        kCal = weight * 33
        fat = int(weight)
        protein = 2 * fat
        carbs = int((kCal - 4 * protein - 9 * fat) / 4)
        sugar = kCal * 0.025
        fiber = kCal * 0.014

        return Macros(
            label = label,
            kCal = kCal,
            fat = fat,
            protein = protein,
            carbs = carbs,
            sugar = sugar,
            fiber = fiber
        )

    def __str__(self):
        return str(values())

    def values(self):
        return {
            "kCal": self.kCal,
            "carbs": self.carbs,
            "fat": self.fat,
            "protein": self.protein,
            "fiber": self.fiber,
            "sugar": self.sugar
        }
