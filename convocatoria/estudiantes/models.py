from django.db import models

class Estudiante(models.Model):
    id_estudiante = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    facultad = models.CharField(max_length=100)
    estado_convocatoria = models.CharField(
        max_length=50,
        choices=[('Pendiente', 'Pendiente'), ('Elegible', 'Elegible'), ('No Elegible', 'No Elegible')],
        default='Pendiente'
    )

    def __str__(self):
        return f"{self.nombre} ({self.estado_convocatoria})"
