from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('urls/<int:isJs>', views.index, name='index'),
    path('newUrl', views.newUrl, name='newUrl'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('<str:shorten>', views.shorten, name='shorten'),
]