from django.shortcuts import render
from coded.models import Event

# Create your views here.


def home(request):
    x = Event.objects.all()
    context = {
        "N": x
    }
    return render(request, 'home.html', context)


def body(request, id):
    x = Event.objects.get(id=id)

    context = {
        "w": x
    }
    return render(request, 'home.html', context)
