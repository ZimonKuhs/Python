"""
@author:  Zimon Kuhs.
@date:    2021-07-09.
"""

from django.http import HttpResponse
from .models import Macros, Person

def nutrition(request):
    return HttpResponse("\"Registration\" goes here.")

def person(request, person_name):
    person = Person.objects.get(name=person_name)
    macros = Macros.objects.get(person_id=person.id)

    message = "%s<br><br>" % person_name
    
    for key in macros.values().keys() :
        message += "%s - %s<br>" % (key, macros.values()[key])
    
    return HttpResponse(message)