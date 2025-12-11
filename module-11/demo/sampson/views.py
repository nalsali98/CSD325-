from django.http import HttpResponse

def index(request):
    return HttpResponse("Al Salihi says Hello!")
