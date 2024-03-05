from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
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


def get_info(request, name):
    names = {
        'denis': 28,
        'kostya': 19,
        'max': 25,
        'anna': 17
    }

    if name in names:
        html_data = f"<p>Возраст пользователя {name} -- {names[name]}"
        return HttpResponse(html_data)
    else:
        raise Http404()  # raising customized error 404
        # return HttpResponseNotFound()  # raising standart error
