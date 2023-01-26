from django.shortcuts import render
from coded.models import Coded

# Create your views here.


def home (request):
    x =Coded.objects.all()
    context = {
        "N" : x
    }
    return render(request,'home.html',context)

def body (request, id):
        x = Coded.objects.get(id = id)

        context = {
            "w" : x
        }
        return render(request,'home.html', context)