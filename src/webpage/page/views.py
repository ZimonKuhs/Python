"""
    General view data control.

    @author:  Zimon Kuhs.
    @date:    2021-07-09.
"""

from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponse("Hello there.")

def gotoIndex(request):
    return HttpResponseRedirect("index")
