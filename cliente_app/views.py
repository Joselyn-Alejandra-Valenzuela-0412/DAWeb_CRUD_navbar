from django.shortcuts import render, redirect
from .models import Cliente


def inicio_vistacliente(request):
    misclientes = Cliente.objects.all()  
    return render(request, "gestionarCliente.html", {"losclientes": misclientes})


def registrarCliente(request):
    if request.method == "POST":
      
        id_cliente = request.POST["txtIdcliente"]
        nombre = request.POST["txtnombre"]
        apellidos = request.POST["txtapellidos"]
        prod_adqu = request.POST["txtprodadqu"]
        tipo_pago = request.POST["txttipopago"]
        num_tel = request.POST["numtelefono"] 
        total_compra = request.POST["numtotalcomp"]

        guardarCliente = Cliente.objects.create(
            id_cliente=id_cliente,
            nombre=nombre,
            apellidos=apellidos,
            prod_adqu=prod_adqu,
            tipo_pago=tipo_pago,
            num_tel=num_tel,
            total_compra=total_compra
        )
        return redirect("cliente")

def seleccionarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    return render(request, "editarCliente.html", {"losclientes": cliente})


def editarCliente(request):
    if request.method == "POST":
        id_cliente = request.POST["txtIdcliente"]
        nombre = request.POST["txtnombre"]
        apellidos = request.POST["txtapellidos"]
        prod_adqu = request.POST["txtprodadqu"]
        tipo_pago = request.POST["txttipopago"]
        num_tel = request.POST["numtelefono"]
        total_compra = request.POST["numtotalcomp"]
  
        cliente = Cliente.objects.get(id_cliente=id_cliente)

        cliente.nombre = nombre
        cliente.apellidos = apellidos
        cliente.prod_adqu = prod_adqu
        cliente.tipo_pago = tipo_pago
        cliente.num_tel = num_tel
        cliente.total_compra = total_compra

        cliente.save()
        return redirect("cliente")

def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("cliente")
