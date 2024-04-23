from django.urls import path
from hm_app import views

urlpatterns = [
    path('', views.index),
    path('producers/', views.producers, name='producers'),
    path('comment_form/', views.comment_form, name='comment_form'),
]