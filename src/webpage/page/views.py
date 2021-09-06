"""
    General view data control.

    @author:  Zimon Kuhs.
    @date:    2021-07-09.
"""

from django.http import HttpResponse, HttpResponseRedirect

"""
    Placeholder view that should not be displayed.

    TODO:   Should redirect to something relevant.

    @param request      The HTTP request sent.
    @return             A redirection response.
"""
def index(request):
    return HttpResponse("Hello there.")

"""
    Redirects from empty URL to index.

    @param request      The HTTP request sent.
    @return             A redirection response.
"""
def gotoIndex(request):
    return HttpResponseRedirect("index")
