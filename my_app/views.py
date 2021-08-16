from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")


def new_search(request):
    return render(request, "new_search.html")