from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
        path('', views.index, name='index'),
        path('request_info/', views.request_info, name='request_info'),
        path('pathview/<str:name>/<int:id>', views.pathview, name='pathview'),
        path('queryview/', views.query_view, name='queryview'),
        path('form_view/', views.form_view, name='form_view'),
]
