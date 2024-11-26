from django.urls import path
from editorial_app import views
urlpatterns = [
    path("editorial",views.inicio_vistaeditorial,name="editorial"),
    path("registrarEditorial/",views.registrarEditorial,name="registrarEditorial"),
    path("seleccionarEditorial/<id_edit>",views.seleccionarEditorial,name="seleccionarEditorial"),
    path("editarEditorial/",views.editarEditorial,name="editarEditorial"),
    path("borrarEditorial/<id_edit>",views.borrarEditorial,name="borrarEditorial")
    
]