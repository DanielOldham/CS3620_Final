from . import views
from django.urls import path

app_name = 'authentication'
urlpatterns = [
    path('', views.login, name='login'),
]