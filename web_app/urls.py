from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_our_files', views.save_our_files, name='save_our_files'),
]