from django.urls import path
from autor_app import views
urlpatterns = [
    path("autor",views.inicio_vistaautor,name="autor"),
    path("registrarAutor/",views.registrarAutor,name="registrarAutor"),
    path("seleccionarAutor/<id_autor>",views.seleccionarAutor,name="seleccionarAutor"),
    path("editarAutor/",views.editarAutor,name="editarAutor"),
    path("borrarAutor/<id_autor>",views.borrarAutor,name="borrarAutor")
    
]