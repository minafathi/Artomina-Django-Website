from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Cat, Paint


def cat_list(request):
    cats = Cat.objects.all()
    return render(request, 'cats/cat_list.html', {'cats':cats, 'nbar':'cat_list'})

def cat_detail(request, pk):
    cat = get_object_or_404(Cat, pk=pk)
    return render(request, 'cats/cat_detail.html', {'cat':cat})

def paint_detail(request, cat_pk, paint_pk):
    paint = get_object_or_404(Paint, cat_id=cat_pk, pk=paint_pk)
    return render(request, 'cats/paint_detail.html', {'paint':paint})

def paint_list(request):
    paints = Paint.objects.all()
    return render(request, 'cats/paint_list.html', {'paints':paints, 'nbar':'album'})

