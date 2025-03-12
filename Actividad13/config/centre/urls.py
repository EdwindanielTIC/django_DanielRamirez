from django.urls import path
from . import views  # Importar las vistas del mismo directorio

urlpatterns = [
    path('', views.index, name='index'),
    path('professors/', views.professors, name='professors'),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('books/book/<str:pk>/', views.book, name='book'),
    path('books/', views.books, name='books'),
]
