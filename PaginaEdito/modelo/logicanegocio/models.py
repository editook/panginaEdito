from django.db import models
##reinicio de todo python manage.py runserver --setting=PaginaEdito.settings.local
# Create your models here.
#python manage.py migrate , makemigrations, modificar el manage direccion
#user : admin, baseedu
class Proyecto(models.Model):
    NombreProyecto = models.CharField(max_length=35)
    Descripcion = models.CharField(max_length=35)
    Fecha = models.DateTimeField(auto_now_add=True)
    LENGUAJE = (('JAVA', 'JAVA-SWING'), ('C', 'VISUAL-STUDIO'))
    LenguajeProgramacion = models.CharField(max_length=4, choices=LENGUAJE, default='JAVA')

    def DatosProyecto(self):
        cadena = "{0} {1} {2} {3}"
        return cadena.format(self.NombreProyecto, self.Descripcion, self.LenguajeProgramacion, self.Fecha)

    def __str__(self):
        return self.DatosProyecto()


class Comentario(models.Model):
    Proyecto = models.ForeignKey(Proyecto, null=False, on_delete=models.CASCADE)
    NumeroIdentificador = models.PositiveSmallIntegerField()
    TipoComentario = models.BooleanField(default=True)
    Mensaje = models.CharField(max_length=100)

    def __str__(self):
        cadena = "{0} => {1} {2}"
        return cadena.format(self.NumeroIdentificador, self.TipoComentario, self.Mensaje)