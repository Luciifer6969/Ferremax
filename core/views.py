from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistrationForm
from .models import Producto,Pedido,Entrega,EstadoEntrega

def index(request):
    return render(request, 'index.html')

def auth_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error = 'Correo o Contraseña incorrecta!'
            return render(request, 'auth_login.html', {'error': error})
    else:
        return render(request, 'auth_login.html')
    
def auth_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ingresado ya existe')
                messages.get_messages(request).used = True
                return redirect('auth_register')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'El correo ingresado ya existe')
                messages.get_messages(request).used = True
                return redirect('auth_register')
            User.objects.create_user(username=username, first_name=name, last_name=last_name, password=password, email=email)
            return redirect('auth_login')
        else:
            messages.error(request, 'Error en el registro. Por favor, corrija los campos resaltados.')
            messages.get_messages(request).used = True
    else:  # GET request or any other method
        form = RegistrationForm()
    
    return render(request, 'auth_register.html', {'form': form}) 

def exit(request):
    logout(request)
    return redirect('auth_login')

def stock_products(request):
    productos = Producto.objects.all()

    if not productos:
        messages.error(request,'No existen productos registrados')
        messages.get_messages(request).used = True

    return render(request,'stock_products.html',{'productos':productos})

def pedidos(request):
    pedidos = Pedido.objects.all()
    estados_pedidos = []

    for pedido in pedidos:
        # Acceder al nombre del estado del pedido para cada pedido
        estado_pedido = pedido.estado.estado
        estados_pedidos.append(estado_pedido)
    if not pedidos:
        messages.error(request,'No existen pedidos')
        messages.get_messages(request).used = True

    return render(request,'pedidos.html',{'pedidos':pedidos,'estados':estados_pedidos})

def solicitud_bodega(request):
    return render(request,'solicitud_bodega.html')

def productos(request):
    productos = Producto.objects.all()
    
    return render(request,'productos.html',{'producto':productos})

def cart(request):
    return render(request,'cart.html')

def entrega(request):
    entregaObj = Entrega.objects.all()
    pedidoList = []
    estados = []
    estadoEntregaObj = EstadoEntrega.objects.all()

    for entrega in entregaObj:
        # Obtener el pedido asociado a esta entrega
        pedido = entrega.pedido   
        pedidoList.append(pedido)
        # Obtener el estado de entrega y agregarlo a la lista de estados
        estadoEntrega = entrega.estado_entrega.estado 
        estados.append(estadoEntrega)

    if not entregaObj:
        messages.error(request,'No existen registros de entrega')
        messages.get_messages(request).used = True

    if not pedidoList:
        messages.error(request,'No existen registros de pedidos') 
        messages.get_messages(request).used = True

    return render(request,'entrega.html',{'estado': estados, 'pedidos': pedidoList,'entrega':entregaObj,'estadoEntrega':estadoEntregaObj})


def edit_entrega(request,id_entrega):
    entregaObj = get_object_or_404(Entrega, id_entrega=id_entrega)
    detail = Entrega.objects.get(id_entrega=entregaObj.id_entrega)
    pedidoObj = Pedido.objects.get(id=detail.id_entrega)
    estadoEntregaObj = EstadoEntrega.objects.all()

    if not detail:
        messages.error(request,'No existen registros de entrega')
        messages.get_messages(request).used = True

    if not pedidoObj:
        messages.error(request,'No existen registros de pedidos') 
        messages.get_messages(request).used = True

    if request.method == 'POST':
        estado_id = request.POST.get('estado')
        pkEstado = EstadoEntrega.objects.get(id=estado_id)
        entregaObj.estado_entrega = pkEstado
        entregaObj.save()
        messages.success(request, 'Entrega registrada correctamente', extra_tags='success')
        messages.get_messages(request).used = True
        return redirect('entrega')
    else:
        return render(request,'editar_entrega.html',{'pedidos': pedidoObj,'entrega':entregaObj,'estadoEntrega':estadoEntregaObj})