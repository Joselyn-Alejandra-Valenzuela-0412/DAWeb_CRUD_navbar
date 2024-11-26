from django.shortcuts import render, redirect
from .models import Manga

# Vista para mostrar todos los mangas
def inicio_vistamanga(request):
    mismangas = Manga.objects.all()  # Asegúrate de llamar al método `.all()`
    return render(request, "gestionarManga.html", {"losmangas": mismangas})

# Vista para registrar un nuevo manga
def registrarManga(request):
    # Capturar los datos enviados desde el formulario
    id_manga = request.POST["txtIdmanga"]
    titulo = request.POST["txttitulo"]
    volumen = request.POST["numvolumen"]
    genero = request.POST["txtgenero"]
    sinopsis = request.POST["txtsinopsis"]
    fecha_publ = request.POST["datefechap"]
    precio = request.POST["numprecio"]

    # Crear y guardar el objeto Manga
    Manga.objects.create(
        id_manga=id_manga,
        titulo=titulo,
        volumen=volumen,
        genero=genero,
        sinopsis=sinopsis,
        fecha_publ=fecha_publ,
        precio=precio,
    )
    return redirect("manga")

# Vista para seleccionar un manga y enviarlo al formulario de edición
def seleccionarManga(request, id_manga):
    manga = Manga.objects.get(id_manga=id_manga)  # Obtener el manga por su ID
    return render(request, "editarManga.html", {"losmangas": manga})  # Enviar el manga al template

# Vista para editar un manga existente
def editarManga(request):
    # Capturar los datos enviados desde el formulario
    id_manga = request.POST["txtIdmanga"]
    titulo = request.POST["txttitulo"]
    volumen = request.POST["numvolumen"]
    genero = request.POST["txtgenero"]
    sinopsis = request.POST["txtsinopsis"]
    fecha_publ = request.POST["datefechap"]
    precio = request.POST["numprecio"]

    # Obtener la instancia del manga y actualizar los datos
    manga = Manga.objects.get(id_manga=id_manga)
    manga.titulo = titulo
    manga.volumen = volumen
    manga.genero = genero
    manga.sinopsis = sinopsis
    manga.fecha_publ = fecha_publ
    manga.precio = precio

    manga.save()  # Guardar los cambios en la base de datos
    return redirect("manga")

# Vista para borrar un manga
def borrarManga(request, id_manga):
    manga = Manga.objects.get(id_manga=id_manga)  # Obtener el manga por su ID
    manga.delete()  # Eliminar el manga
    return redirect("manga")
