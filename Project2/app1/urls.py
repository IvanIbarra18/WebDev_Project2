from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view),
    path('movies/', views.movies_view),
]