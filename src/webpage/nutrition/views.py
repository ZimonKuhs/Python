from django.http import HttpResponse

def nutrition(request):
    return HttpResponse("Hello, fuckers!<br><br>Time for some excessive nutritional data...")

def data(request):
    return HttpResponse("Test is successful. Bummer.")