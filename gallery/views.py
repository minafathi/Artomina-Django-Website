from django.shortcuts import render
from cats.models import Cat

def hello_world(request):
    cats = Cat.objects.all()
    return render(request, 'home.html', {'cats':cats, 'nbar': 'home'})

