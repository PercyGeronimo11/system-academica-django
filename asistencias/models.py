from django.db import models

class Alumno(models.Model):
    name=models.CharField(max_length=100)
    surname_mother= models.CharField(max_length=100)
    surname_father= models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    grade_section_current = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1)
    status = models.BooleanField(default=True)
    qr_code = models.CharField(max_length=255, unique=True)


    class Meta:
        db_table = 'students'       # Nombre de la tabla en la base de datos
        managed = False     # No administrar la tabla con migraciones de Django

    def __str__(self):
        return f"{self.name} {self.surname_mother} {self.surname_father}"


class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, db_constraint=False)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, default='1')  # '1' para presente, '0' para ausente
    class Meta:
        db_table = 'assistances_general'    # Nombre de la tabla en la base de datos