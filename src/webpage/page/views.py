"""
@author:  Zimon Kuhs.
@date:    2021-07-09.
"""

from django.http import HttpResponse

def index(request):
    return HttpResponse("You shouldn't be here...")