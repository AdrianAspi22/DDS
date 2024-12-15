from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudiante

def registrar_estudiante(request):
    if request.method == 'POST':
        id_estudiante = request.POST['id_estudiante']
        nombre = request.POST['nombre']
        facultad = request.POST['facultad']
        
        estado = 'Elegible' if facultad in ['Ingeniería', 'Ciencias'] else 'No Elegible'
        
        estudiante = Estudiante(
            id_estudiante=id_estudiante,
            nombre=nombre,
            facultad=facultad,
            estado_convocatoria=estado
        )
        estudiante.save()
        return redirect('listar_estudiantes')
    return render(request, 'estudiantes/registrar.html')

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/listar.html', {'estudiantes': estudiantes})

def procesar_convocatoria(request, id_estudiante):
    estudiante = get_object_or_404(Estudiante, id_estudiante=id_estudiante)
    if estudiante.estado_convocatoria == 'Elegible':
        estudiante.estado_convocatoria = 'Aceptado'
    else:
        estudiante.estado_convocatoria = 'Rechazado'
    estudiante.save()
    return redirect('listar_estudiantes')
