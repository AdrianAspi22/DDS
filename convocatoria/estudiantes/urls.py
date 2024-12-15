from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_estudiante, name='registrar_estudiante'),
    path('listar/', views.listar_estudiantes, name='listar_estudiantes'),
    path('procesar/<str:id_estudiante>/', views.procesar_convocatoria, name='procesar_convocatoria'),
]
