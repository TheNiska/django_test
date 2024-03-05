from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.
def index(request):
    url = reverse("txtapp:index")
    html = f'''\
    <h1>Index page of TXTAPP</h1>
    <p>Some paragraph</p>
    <p>The path is {url}</p>
    '''
    return HttpResponse(html)
