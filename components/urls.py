from . import views
from django.urls import path

app_name = 'components'
urlpatterns = [
    path('', views.list, name='dashboard'),
]