from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_pelicula>/', views.view_pelicula, name='view_pelicula'),
    path('add/', views.add, name='add'),
    path('edit/<int:id_pelicula>/', views.edit, name='edit'),  
    path('delete/<int:id_pelicula>/', views.delete, name='delete'),  
]
