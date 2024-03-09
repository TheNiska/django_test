from django.urls import path
from . import views

app_name = 'first_app'  # views of this app indentified by this name

urlpatterns = [
        path('', views.index, name='index'),
        path('request_info/', views.request_info, name='request_info'),
        path('pathview/<str:name>/<int:id>', views.pathview, name='pathview'),
        path('queryview/', views.query_view, name='queryview'),
        path('form_view/', views.form_view, name='form_view'),
        path('menu/', views.menu_by_id, name='menu'),
        path('home/', views.home, name='home'),
        path('register/', views.register, name='register'),
        path('login/', views.login, name='login'),
]
