from django.shortcuts import render
from .models import Me

def me(request):
    me = Me.objects.all()
    return render(request, 'aboutme/me.html', {'me':me, 'nbar':'aboutme'})
