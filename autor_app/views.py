from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor


# Vista para listar autores
def inicio_vistaautor(request):
    misautores = Autor.objects.all()  # Obtiene todos los autores
    return render(request, "gestionarAutor.html", {"losautores": misautores})


# Vista para registrar un nuevo autor
def registrarAutor(request):
    if request.method == "POST":
        id_autor = request.POST["txtIdautor"]
        id_edit = request.POST["txtidedit"]
        id_manga = request.POST["txtidmanga"]
        nombre = request.POST["txtnombre"]
        apellidos = request.POST["txtapellidos"]
        foto = request.FILES.get("foto", None)
        estado = request.POST["txtestado"]
        nacionalidad = request.POST["txtnacional"]
        num_tel = request.POST["numtel"]
        correo = request.POST["txtcorreo"]
        ciudad = request.POST["txtciudad"]

        # Creación de nuevo autor
        Autor.objects.create(
            id_autor=id_autor,
            id_edit=id_edit,
            id_manga=id_manga,
            nombre=nombre,
            apellidos=apellidos,
            foto=foto,
            estado=estado,
            nacionalidad=nacionalidad,
            num_tel=num_tel,
            correo=correo,
            ciudad=ciudad,
        )
        return redirect("autor")

    return render(request, "registrarAutor.html")


# Vista para seleccionar un autor para editar
def seleccionarAutor(request, id_autor):
    autor = get_object_or_404(Autor, id_autor=id_autor)  # Obtiene el autor o 404 si no existe
    return render(request, "editarAutor.html", {"losautores": autor})


# Vista para editar un autor existente
def editarAutor(request):
    if request.method == "POST":
        id_autor = request.POST["txtIdautor"]
        id_edit = request.POST["txtidedit"]
        id_manga = request.POST["txtidmanga"]
        nombre = request.POST["txtnombre"]
        apellidos = request.POST["txtapellidos"]
        foto = request.FILES.get("foto")
        estado = request.POST["txtestado"]
        nacionalidad = request.POST["txtnacional"]
        num_tel = request.POST["numtel"]
        correo = request.POST["txtcorreo"]
        ciudad = request.POST["txtciudad"]

        # Obtiene el autor a editar
        autor = get_object_or_404(Autor, id_autor=id_autor)

        # Actualiza los campos del autor
        autor.id_edit = id_edit
        autor.id_manga = id_manga
        autor.nombre = nombre
        autor.apellidos = apellidos
        if foto:  # Si se proporciona una nueva foto
            autor.foto = foto
        autor.estado = estado
        autor.nacionalidad = nacionalidad
        autor.num_tel = num_tel
        autor.correo = correo
        autor.ciudad = ciudad

        autor.save()  # Guarda los cambios
        return redirect("autor")

    return render(request, "editarAutor.html")



def borrarAutor(request, id_autor):
    autor = get_object_or_404(Autor, id_autor=id_autor)  
    autor.delete()  # Borra el autor
    return redirect("autor")
