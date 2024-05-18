from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistrationForm
from .models import Producto,Pedido,Entrega,EstadoEntrega,DetallePedido
from django.contrib.auth.decorators import login_required
from .cart import Cart
import json
import http.client
import mercadopago



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
    return render(request, 'productos.html',{'producto':productos})



@login_required
def cart(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    productoCart = cart.get_prodss()

    ##clave produccion de usuario de prueba TESTUSER1085505293 pass : Hb9QJvAszT || revisar cuenta mercado pago siempre si tiene saldo
    sdk = mercadopago.SDK("APP_USR-170340208437871-051617-b45127860d141be852b0d15af556090e-1817032202")
    items = []

    for product_id, details in productoCart.items():
        product = details['product']

        try:
            quantity = details['quantity']
            unit_price = float(details['precio'])
        except (ValueError, TypeError) as e:
            print(f"Error en conversión de cantidad o precio: {e}")
            continue 

        items.append({
            "title": product.nombre,  # Asumiendo que tu modelo Producto tiene un campo nombre
            "quantity": quantity,
            "unit_price": unit_price,
        })
    
    preference_data = {
        "back_urls": {
            "success": "http://127.0.0.1:8000/success_pay/"
        },
        "items": items
    }
    
    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    return render(request,'cart.html',{'productos':cart_products,'preference':preference})


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
    
#agregar producto a la sesion
def agregar_producto(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productoId'))
        product = get_object_or_404(Producto, id=product_id)
        cart.add(product=product)
        # response = JsonResponse({'Product name': product.nombre})

        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})

        return response 
       
#actualizar producto a la sesion    
def update_producto(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productoId'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id,quantity=product_qty)
        response = JsonResponse({'cantidadProd':product_qty})     
        return response
    
#eliminar producto de la sesion 
def delete_producto(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productoId'))
        cart.delete(product=product_id)
        response = JsonResponse({'product':product_id})

    return response



def verProducto(request, producto_id):
    producto = Producto.objects.get(id = producto_id)
    if request.method == 'POST':    
        response = obtenerValoresApi(request,producto)
        data = json.loads(response.content.decode('utf-8'))
        nuevo_precio = data.get('nuevo_precio')

        return render(request, 'producto.html',{'producto':producto,'nuevo_precio':nuevo_precio})
    else:
        return render(request, 'producto.html',{'producto':producto})
    
def contact(request):
    producto = Producto.objects.all()

    if request.method == 'POST':
        motivo = request.POST['motivo']
        productoId = request.POST['productoId']
        comment = request.POST['comment']

        messages.success(request, 'Registro añadido correctamente')
        messages.get_messages(request).used = True
        return redirect('contact')
    else:
        return render(request, 'contact.html',{'producto':producto})

def obtenerValoresApi(request,producto):
    nuevo_precio = None 
    if request.method == 'POST':
        tipo_moneda = request.POST.get('tipo_moneda')
        producto_id = request.POST.get('producto_id')
        productObj = Producto.objects.get(id= producto_id)

        #consumo de la API
        url = "mindicador.cl"
        connection = http.client.HTTPSConnection(url)
        connection.request('GET', '/api')
        response = connection.getresponse()
        data = json.loads(response.read().decode('utf-8'))
        DataList = []

        for key, value in data.items():
            DataList.append(value)
        
        dolar = None
        uf = None
        euro = None
        utm = None

        #iterar el objeto para cada valor 
        for item in DataList:
            if isinstance(item, dict):
                if item.get('codigo') == 'dolar':
                    dolar = item.get('valor')
                elif item.get('codigo') == 'uf':
                    uf = item.get('valor')
                elif item.get('codigo') == 'euro':
                    euro = item.get('valor')
                elif item.get('codigo') == 'utm':
                    utm = item.get('valor')
                    
        #obtener id de producto       
        if tipo_moneda == 'dolar': 
            nuevo_precio = int(float(producto.precio) / float(dolar))
        elif tipo_moneda == 'uf':
            nuevo_precio = int(float(producto.precio) / float(uf))
        elif tipo_moneda == 'euro':
            nuevo_precio = int(float(producto.precio) / float(euro))
        elif tipo_moneda == 'utm':
            nuevo_precio = int(float(producto.precio) / float(utm))
        else:
            nuevo_precio = productObj.precio
        response_data = {'nuevo_precio': nuevo_precio}
        print("Datos de respuesta:", response_data)
        return JsonResponse(response_data) 
    else:
        return print('nofunciono')
    
def success_pay(request):
    collection_id = request.GET.get('collection_id')
    collection_status = request.GET.get('collection_status')
    payment_id = request.GET.get('payment_id')
    status = request.GET.get('status')
    external_reference = request.GET.get('external_reference')
    payment_type = request.GET.get('payment_type')
    merchant_order_id = request.GET.get('merchant_order_id')
    preference_id = request.GET.get('preference_id')
    site_id = request.GET.get('site_id')
    processing_mode = request.GET.get('processing_mode')
    merchant_account_id = request.GET.get('merchant_account_id') 

    context = {
        'collection_id': collection_id,
        'collection_status': collection_status,
        'payment_id': payment_id,
        'status': status,
        'external_reference': external_reference,
        'payment_type': payment_type,
        'merchant_order_id': merchant_order_id,
        'preference_id': preference_id,
        'site_id': site_id,
        'processing_mode': processing_mode,
        'merchant_account_id': merchant_account_id,
    }

    return render(request,'success_pay.html',context)    

