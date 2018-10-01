from django.urls import path

from . import views

urlpatterns = [
    path('<str:entry1>/hello_name', views.hello, name='name'),
    path('<int:num1>/times2', views.times2, name='times2'),
    path('<int:num1>/sum', views.sum, name='sum')
]