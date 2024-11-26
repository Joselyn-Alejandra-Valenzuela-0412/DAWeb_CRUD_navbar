from django.shortcuts import render,redirect
from .models import Venta
# Create your views here.

def inicio_vistaventa(request):
    misventas=Venta.objects.all()
    return render(request,"gestionarVenta.html",{"lasventas":misventas})


def registrarVenta(request):
    id_venta=request.POST["txtIdventa"]
    id_manga=request.POST["txtidmanga"]
    id_emp=request.POST["txtidemp"]
    id_cliente=request.POST["txtidcliente"]
    cantidad=request.POST["numcantidad"]
    total=request.POST["numtotal"]
    fecha_venta=request.POST["datefechaventa"]

    guardarVenta=Venta.objects.create(id_venta=id_venta,id_manga=id_manga,id_emp=id_emp,id_cliente=id_cliente,cantidad=cantidad,total=total,fecha_venta=fecha_venta)
    return redirect("venta")

def seleccionarVenta(request,id_venta):
    venta=Venta.objects.get(id_venta=id_venta)
    return render(request,"editarVenta.html",{"lasventas":venta})

def editarVenta(request):
    id_venta=request.POST["txtIdventa"]
    id_manga=request.POST["txtidmanga"]
    id_emp=request.POST["txtidemp"]
    id_cliente=request.POST["txtidcliente"]
    cantidad=request.POST["numcantidad"]
    total=request.POST["numtotal"]
    fecha_venta=request.POST["datefechaventa"]

    venta=Venta.objects.get(id_venta=id_venta)
    venta.id_manga=id_manga
    venta.id_emp=id_emp
    venta.id_cliente=id_cliente
    venta.cantidad=cantidad
    venta.total=total
    venta.fecha_venta=fecha_venta
    
    venta.save()
    return redirect("venta")

def borrarVenta(request,id_venta):
    venta=Venta.objects.get(id_venta=id_venta)
    venta.delete()
    return redirect("venta")
