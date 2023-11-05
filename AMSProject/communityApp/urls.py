from django.urls import path
from . import views

app_name = 'communityApp'


urlpatterns = [
    path('', views.index, name='index'),
]
