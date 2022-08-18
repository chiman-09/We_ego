from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register',views.register),
    path('register_submit',views.index),
    path('search', views.search),
    path('search_result',views.search_user)

]

