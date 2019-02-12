from django.db import models

# Create your models here.
#el nombre de las clases siempre van en singular
# y Hacemos que herede de la super clase Models.model 
#esta clase representa una tabla en la base de datos
#una tabla tiene filas y columnas
#cada atributo de esta clase representa una columna en la tabla de la DB
class Project(models.Model):
    #campo cadena de caracteres
    title = models.CharField(max_length=200, verbose_name="Titulo")
    #campo de texto
    description = models.TextField(verbose_name="Descripción")
    #campo de imagen
    image = models.ImageField(verbose_name="Imágen", upload_to="projects")
    link = models.URLField(verbose_name="Direccion web",null=True, blank=True)
    #fecha que se creo el modelo
    #el atributo que se le agrego nos dice que el campo created
    # se añadirá la hora automáticamente cuando se crea la primera vez
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    #fecha que se actualizó el modelo
    #aqui la diferencia entre el atributo de arriba es que el auto_now se ejecuta cada vez
    # que se actualiza una instancia y el anterior solo se ejecuta una vez cuando se crea
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")
   

    class Meta: 
        #agregamos el atributo
        verbose_name="proyecto"
        #segundo atributo para ponerlo en plural, si no lo asigamos
        #directamente añade una (s) al final del nombre pero podriamos necesitar
        #declararlo
        verbose_name_plural="proyectos" 
        #Tambien es aconsejable poner un campo de ordenación por defecto para nuestros registros
        #que en nuestro caso sería la fecha de creación.
        #pero no vamos a ordenar de mas antiguo al mas nuevo como Django lo hace por defecto si no que vamos ordenar del mas reciente al mas antiguo
        # y esto se hace solamente colocando un guion delante del nombre que queremos ordenar
        ordering=["-created"]

        #le pasamos self como si fuera una clase normal de toda la vida
        #hacemos un return haciendo referencia al self.title que es el nombre de nuestro proyecto
        #y con esto ya nos devolverá el nombre de nuestro proyecto
    def __str__(self):
        return self.title


           


