from django.shortcuts import render, redirect
from .models import Empleado  # Assuming you have an Empleado model

# Vista para mostrar todos los empleados
def inicio_vistaempleado(request):
    mis_empleados = Empleado.objects.all()  # Asegúrate de llamar al método `.all()`
    return render(request, "gestionarEmpleado.html", {"losempleados": mis_empleados})

# Vista para registrar un nuevo empleado
def registrarEmpleado(request):
    # Capturar los datos enviados desde el formulario
    id_emp = request.POST["txtidemp"]
    nombre = request.POST["txtnombre"]
    apellidos = request.POST["txtapellidos"]
    direccion = request.POST["txtdirecc"]
    telefono = request.POST["numtelefono"]
    area_gen = request.POST["txtareagen"]
    sueldo = request.POST["numsueldo"]

    # Crear y guardar el objeto Empleado
    Empleado.objects.create(
        id_emp=id_emp,
        nombre=nombre,
        apellidos=apellidos,
        direccion=direccion,
        telefono=telefono,
        area_gen=area_gen,
        sueldo=sueldo,
    )
    return redirect("empleado")  # Redirige al listado de empleados

# Vista para seleccionar un empleado y enviarlo al formulario de edición
def seleccionarEmpleado(request, id_emp):
    empleado = Empleado.objects.get(id_emp=id_emp)  # Obtener el empleado por su ID
    return render(request, "editarEmpleado.html", {"losempleados": empleado})  # Enviar el empleado al template

# Vista para editar un empleado existente
def editarEmpleado(request):
    # Capturar los datos enviados desde el formulario
    id_emp = request.POST["txtidemp"]
    nombre = request.POST["txtnombre"]
    apellidos = request.POST["txtapellidos"]
    direccion = request.POST["txtdirecc"]
    telefono = request.POST["numtelefono"]
    area_gen = request.POST["txtareagen"]
    sueldo = request.POST["numsueldo"]

    # Obtener la instancia del empleado y actualizar los datos
    empleado = Empleado.objects.get(id_emp=id_emp)
    empleado.nombre = nombre
    empleado.apellidos = apellidos
    empleado.direccion = direccion
    empleado.telefono = telefono
    empleado.area_gen = area_gen
    empleado.sueldo = sueldo

    empleado.save()  # Guardar los cambios en la base de datos
    return redirect("empleado")  # Redirige al listado de empleados

# Vista para borrar un empleado
def borrarEmpleado(request, id_emp):
    empleado = Empleado.objects.get(id_emp=id_emp)  # Obtener el empleado por su ID
    empleado.delete()  # Eliminar el empleado
    return redirect("empleado")  # Redirige al listado de empleados
