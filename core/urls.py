from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('prices/', views.price, name='prices'),
    path('reviews/', views.review, name='reviews'),
    path('contacts/', views.contact, name='contacts')
]
