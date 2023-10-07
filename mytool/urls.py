from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('encrypt', views.encrypt, name='encrypt'),
    path('decrypt', views.decrypt, name='decrypt'),
    path('base64encode', views.base64encode, name='base64encode'),
    path('base64decode', views.base64decode, name='base64decode'),
    path('admin/', admin.site.urls),
]