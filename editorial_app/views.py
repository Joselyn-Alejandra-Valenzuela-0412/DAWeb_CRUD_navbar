from django.shortcuts import render,redirect
from .models import Editorial
# Create your views here.

def inicio_vistaeditorial(request):
    miseditoriales=Editorial.objects.all
    return render(request,"gestionarEditorial.html",{"laseditoriales":miseditoriales})


def registrarEditorial(request):
    id_edit=request.POST["txtIdeditorial"]
    nombre=request.POST["txtnombre"]
    pais=request.POST["txtpais"]
    anio_fundac=request.POST["dateaniofundac"]
    fundador=request.POST["txtfundador"]
    correo=request.POST["txtcorreo"]
    proyectos=request.POST["txtproyectos"]

    guardarEditorial=Editorial.objects.create(id_edit=id_edit,nombre=nombre,pais=pais,anio_fundac=anio_fundac,fundador=fundador,correo=correo,proyectos=proyectos)
    return redirect("editorial")

def seleccionarEditorial(request,id_edit):
    editorial=Editorial.objects.get(id_edit=id_edit)
    return render(request,"editarEditorial.html",{"laseditoriales":editorial})

def editarEditorial(request):
    id_edit=request.POST["txtIdeditorial"]
    nombre=request.POST["txtnombre"]
    pais=request.POST["txtpais"]
    anio_fundac=request.POST["dateaniofundac"]
    fundador=request.POST["txtfundador"]
    correo=request.POST["txtcorreo"]
    proyectos=request.POST["txtproyectos"]

    editorial=Editorial.objects.get(id_edit=id_edit)
    editorial.nombre=nombre
    editorial.pais=pais
    editorial.anio_fundac=anio_fundac
    editorial.fundador=fundador
    editorial.correo=correo
    editorial.proyectos=proyectos
    
    editorial.save()
    return redirect("editorial")

def borrarEditorial(request,id_edit):
    editorial=Editorial.objects.get(id_edit=id_edit)
    editorial.delete()
    return redirect("editorial")
