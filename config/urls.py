from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('cs50wfinal.urls')),
    path('admin/', admin.site.urls),
]