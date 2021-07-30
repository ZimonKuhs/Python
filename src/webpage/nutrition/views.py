"""
@author:  Zimon Kuhs.
@date:    2021-07-09.
"""

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.utils import timezone

from .models import Macros, Person


def index(request):
    return HttpResponseRedirect("register")

def register(request):
    print(request.POST)
    return render(request, "nutrition/register.html")

def registerNew(request):
    newName = request.POST["person_name"]
    newWeight = float(request.POST["person_weight"])
    newWeight = newWeight if request.POST["unit"] == "kg" else newWeight * 2.2

    print("%s %f" % (newName, newWeight))

    if Person.objects.filter(name = newName).count() > 0:
        return render(request, "nutrition/register.html", {
            "name": newName,
            "error_message": "\"%s\" is already registered!" % newName,
        })

    person = Person.objects.create(name = newName, weight = newWeight, register_date = timezone.now())
    macros = Macros.auto(newWeight)
    macros.person = person
    macros.save()

    person.macros_set.add(macros)
    person.save()

    return HttpResponseRedirect(reverse("nutrition:person", args=(newName,)))

def person(request, personName):
    person = get_object_or_404(Person, name = personName)
    macros = person.macros_set.all()

    print(macros)

    context = {
        "name": personName,
        "macros_set": macros
    }

    return render(request, "nutrition/macros.html", context)
