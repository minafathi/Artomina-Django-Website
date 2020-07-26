from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Content

def content_list(request):
    contents = Content.objects.all()
    return render(request, 'contents/content_list.html', {'contents':contents, 'nbar':'content_list'})

def content_detail(request, pk):
    content = get_object_or_404(Content, pk=pk)
    return render(request, 'contents/content_detail.html', {'content':content})

