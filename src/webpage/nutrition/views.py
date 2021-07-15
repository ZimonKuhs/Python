"""
@author:  Zimon Kuhs.
@date:    2021-07-09.
"""

from django.shortcuts import get_object_or_404, render
from .models import Person

def nutrition(request):
    return render(request, "nutrition/redirect.html", {})

def person(request, person_name):
    person = get_object_or_404(Person, name=person_name)
    macros = person.macros_set.all()

    print(macros)

    context = {
        "name":       person_name,
        "macros_set": macros
    }
    
    return render(request, "nutrition/macros.html", context)

def register(request):
    return render(request, "nutrition/register.html", {})