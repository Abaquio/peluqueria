from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app.models import Servicio, Cliente, Empleado, Atencion
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')

def servicios(request):
    serv = Servicio.objects.all()

    data = {'servicios':serv}


    return render(request,'app/servicios.html',data)

from django.shortcuts import render
from .models import Cliente, Servicio, Atencion

def reservas(request):
    if request.method == 'POST':
        # datos del formulario
        nombre = request.POST.get('first-name')
        apellido = request.POST.get('last-name')
        fono = request.POST.get('fono')
        correo = request.POST.get('email')
        servicio_id = request.POST.get('servicio')
        fecha = request.POST.get('fecha')

        # --- cliente ---
        cliente = Cliente(nombre=nombre, apellido=apellido, fono=fono, correo=correo)
        cliente.save()

        # --- id del servicio ---
        if servicio_id is not None:
            try:
                servicio_id = int(servicio_id)
                servicio = Servicio.objects.get(ids=servicio_id)

                # --- atencion y relaciones ---
                atencion = Atencion(
                    fecha=fecha,
                    estado="Pendiente",
                    reserva=True,
                    servicio_ids=servicio,
                    cliente_rut_c=cliente
                )

                atencion.save()

            except ValueError:
                # Manejar la excepción si la conversión a entero falla
                # Puedes imprimir un mensaje de depuración o manejarlo según tus necesidades
                print("Error: servicio_id no es un número entero")
        else:
            # Manejar el caso en el que servicio_id es None
            # Puedes imprimir un mensaje de depuración o manejarlo según tus necesidades
            print("Error: servicio_id es None")

    # Obtener todos los servicios para pasarlos a la plantilla
    servicios = Servicio.objects.all()
    data = {'servicios': servicios}
    return render(request, 'app/reservas.html', data)

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect ('/dashboard')
    return render(request, 'app/login.html')

def dashboard(request):
    serv = Servicio.objects.all()

    data = {'servicios':serv}


    return render(request,'app/servicios.html',data)