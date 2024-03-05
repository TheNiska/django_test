from django.urls import path
from . import views

app_name = 'txtapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('info/<str:name>', views.get_info, name='info'),
]
