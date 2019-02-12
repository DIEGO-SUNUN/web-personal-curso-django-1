from django.contrib import admin

#importamos el modelo (.models haciendo referencia a la propia app
# por que estamos haciendo referencia a un fichero que esta en el mismo direcorio )
from .models import Project
# Register your models here.
#ahora para registrarlo (dentro del parentisis el nombre del moedelo que vamos a registrar)



#colocamos una clase para extender el panel de administración de admin,
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
#esto es una lista o una tupla que vamos a redefinir diciendole los campos que
#son solo de lectura para que se muestren en el panel de administrador

admin.site.register(Project, ProjectAdmin)