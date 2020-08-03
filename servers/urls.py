from django.urls import path

from . import views

app_name = 'servers'
urlpatterns = [
    path('', views.index, name='index'),
]