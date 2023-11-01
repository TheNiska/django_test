from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello. This is the index view of my first app.")

def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    msg = (
        f"Path: {path}<br>"
        f"Scheme: {scheme}<br>"
        f"Method: {method}<br>"
        f"Address: {address}<br>"
        f"User agent: {user_agent}<br>"
        f"Path info: {path_info}<br>"
    )

    return HttpResponse(msg, content_type='text/html', charset='utf-8')
