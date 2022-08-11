from django.urls import include, path
from .import views

urlpatterns = [
    path('all/', views.index, name='allpost'),
    path('details/', views.details, name='postdetails'),

    ]