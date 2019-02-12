"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views

#esto es para ir a buscar dentro de la configuración de django settings.py
#esto habra cargado el fichero settings.py dentro de la memoria
#ahora podremos ingresar a las variables MEDIA_URL  Y  MEDIA_ROOT
from django.conf import settings

urlpatterns = [
    #como quiero que sea la raiz del sitio web (Portada) lo dejo vacío y no le hago referencia 
    path('', core_views.home, name="home"),
    path('about-me/', core_views.about, name="about"),
    path('portfolio/', portfolio_views.portfolio, name="portfolio"),
    path('contact/', core_views.contact, name="contact" ),
    
    #dirección url apuntando al admin cargando un se t de direcciones internas
    #puede cambiarse el nombre del enlace, nosotros lo establecemos
    path('admin/', admin.site.urls),

]
#esto estará mirando del fichero settings.py la variable DEBUG
#si es verdadero por que todo esto solamente funciona cuando 
# estemos en modo DEBUG. e importamos la configuración extendida 
#para servir ficheros estáticos (medias)
if settings.DEBUG:
    from django.conf.urls.static import static
#una ves que cargamos static que nos permite cargar ficheros estaticos 
#tenemos que decirle a las urlspatterns(patrones de urls) que si 
#alguien intenta acceder a la dirección /media/projects/nombrefichero.jpg
#le sirva el la imagen o el fichero de turno entonces lo agregamos al 
#urlpatterns el nuevo patron que en lugar de hacer un path normal, primero 
#le pasaríamos la url donde queremos servir los ficheros media que es media
#pero lo vamos a importar de settings.py que por algo lo hemos configurado alli
 # y luego le tenemos que pasar algo llamado el document_root que es la raíz
 #donde tiene que ir a encontrar estos ficheros media 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
