from django.urls import path
from . import views  # Importar las vistas del mismo directorio

urlpatterns = [
    path('', views.index, name='index'),
    path('professors/', views.professors, name='professors'),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('user-form/', views.user_form, name='user_form'),
    path('professor_form/', views.professor_form, name='professor_form'),

    # path('details/', views.details(), name='professor_form'),

    path('details/<int:pk>/', views.details, name='details'),
    path('professors/<int:pk>/', views.detailsProfesors, name='detailsProfesors'),
]



