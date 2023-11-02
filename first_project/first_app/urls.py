from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
        path('', views.index, name='index'),
        path('home/', views.home, name='home'),
        path('pathview/<str:name>/<int:id>', views.pathview, name='pathview'),
        path('queryview/', views.query_view, name='queryview'),
        path('showform/', views.show_form, name='showform'),
]

