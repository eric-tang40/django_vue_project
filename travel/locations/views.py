from django.shortcuts import render

def index(request):
    return render(request, "locations/index.html")

# Create your views here.
