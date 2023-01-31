from django.shortcuts import render, redirect
from coded.models import Event
from coded import forms
# Create your views here.


def get_home(request):
    events = Event.objects.all()
    context = {
        "events": events
    }
    return render(request, "home.html", context)


# Create your views here.

def createevents(request):
    form = forms.EventForm()
    if request.method == "POST":
        form = forms.EventForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        "eventform": form
    }
    return render(request, "createevent.html", context)


# def get_events(request):
#     context = {
#         "events": Event.objects.all()
#     }
#     return render(request, 'home.html', context)


def myprofile(request):
    context = {
        "events": Event.objects.all()
    }
    return render(request, 'event.html', context)


def nono(request):
    return render(request, "home")

def get_event(request, obj_id):
    event = Event.objects.get(id=obj_id)
    context = {
        "event" : event
    }
    return render(request, 'event.html', context)


def editevent(request,id):
    edit = Event.objects.get(id=id)

    form = forms.EventForm(instance=edit)
    if request.method == "POST":
        form = forms.EventForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {
        "obj": edit,
        "form": form,
    }
    return render(request, 'editevent.html', context)

def deletevent(request,id):
    Event.objects.get(id=id).delete()
    return redirect("home")

