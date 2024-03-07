from django.shortcuts import render
from django.http import HttpResponse
from first_app.forms import LogForm
from django.urls import reverse
from django.core.exceptions import PermissionDenied


def index(request):
    url = reverse("first_app:index")
    html = f'''\
    <h1>Index page of MAINAPP</h1>
    <p>Some paragraph</p>
    <p>The path is {url}</p>
    '''
    if request.user.is_anonymous:
        raise PermissionDenied()
    elif request.user.has_perm("first_app.can_change_website"):
        html += "<p>Есть права на изменение веб-сайта"\
                f" у {request.user.username}</p>"
    else:
        html += "<p>Нет прав на изменение сайта"\
                f" у {request.user.username}</p>"

    return HttpResponse(html)


def request_info(request):
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


def pathview(request, name, id):
    return HttpResponse(f"These are path parameters: {name}, {id}")


def query_view(request):
    name = request.GET['name']
    id = request.GET['id']

    return HttpResponse(f"These are query parameters: {name}, {id}")


def form_view(request):
    form = LogForm()

    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "home.html", context)
