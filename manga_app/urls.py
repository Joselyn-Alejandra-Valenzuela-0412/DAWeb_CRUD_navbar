from django.urls import path
from manga_app import views

urlpatterns = [
    path("manga",views.inicio_vistamanga,name="manga"),
    path("registrarManga/",views.registrarManga,name="registrarManga"),
    path("seleccionarManga/<id_manga>",views.seleccionarManga,name="seleccionarManga"),
    path("editarManga/",views.editarManga,name="editarManga"),
    path("borrarManga/<id_manga>",views.borrarManga,name="borrarManga")
    
]