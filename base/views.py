from django.shortcuts import render
from .models import Character
from .models import Place
from .models import Organization


def htmdata(request):
    characters = Character.objects.order_by('name')
    places = Place.objects.order_by('name')
    organizations = Organization.objects.order_by('name')
    return render(request, 'index.html', {'characters' : characters, 'places' : places, 'organizations' : organizations})
