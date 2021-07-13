from django.http import HttpResponse

def index(request):
    return HttpResponse("You shouldn't be here...")