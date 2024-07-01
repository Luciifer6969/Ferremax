from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
import requests
from .forms import RegistrationForm
from .models import EstadoPedido, Producto,Pedido,Entrega,EstadoEntrega,Contact,Marca,TipoProducto,DetallePedido
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
 #Agregar al html botones para aprobar o rechazar pedidos. 
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

# views.py
from django.shortcuts import render
from .models import Producto, TipoProducto

def productos(request):
    tipo_producto_id = request.GET.get('tipo_producto')
    productos = Producto.objects.all()
    categoria = None
    
    if tipo_producto_id:
        try:
            tipo_producto_id = int(tipo_producto_id)
            categoria = Producto.objects.filter(tipo_producto_id=tipo_producto_id)
        except ValueError:
            pass  # Si no es un entero, no hace nada adicional
    
    tipos_producto = TipoProducto.objects.all()
    context = {
        'productos': productos if categoria is None else categoria,
        'tipos_producto': tipos_producto,
        'categoria_actual': tipo_producto_id if categoria else None,
    }
    return render(request, 'productos.html', context)




@login_required
def cart(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    productoCart = cart.get_prodss()
    total = cart.cart_total()
    cantidad = cart.get_quants 
    userId = request.user
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
        #Crear objeto de pedido en el for de items con estado pendiente, Agregar formulario de fecha a la tabla entrega y html (Crear formulario y dejar como defecto el estado de entrega por confirmar (?) )
    preference_data = {
        "back_urls": {
            "success": "http://127.0.0.1:8000/success_pay/",
        },
        "items": items
    }
    
    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    print(items)
    print(cantidad)
    for item in items:
        pedidoObj = Pedido(
            User=userId,
            nombre=item["title"],
            estado=EstadoPedido.objects.get(id=1),
            cantidad_producto=item["quantity"],
            precio_producto=item["unit_price"]
        )
        pedidoObj.save()

    return render(request,'cart.html',{'productos':cart_products,'preference':preference,'items':cantidad,'total':total})


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

        #obtener producto de id 
        productObj = Producto.objects.get(id=productoId) 

        contact = Contact(
            motivo=motivo,
            producto=productObj,
            usuario=request.user,
            comentario=comment,
        )
        contact.save()
        messages.success(request, 'Registro añadido correctamente')
        messages.get_messages(request).used = True
        return redirect('contact')
    else:
        return render(request, 'contact.html',{'producto':producto})

def consulta_cliente(request):
    consultas = Contact.objects.all()
    if request.method == 'POST':
        respuesta = request.POST['respuesta']
        contact_id = request.POST['contact_id']
        contact = Contact(
            respuesta = respuesta
        )
        contact = get_object_or_404(Contact, id=contact_id)
        contact.respuesta = respuesta
        contact.save()

    return  render(request, 'consultas_cliente.html',{'data':consultas})

def mis_consultas(request,user_id):
    userObj = User.objects.get(id=user_id)
    data = Contact.objects.filter(usuario= userObj)

    return render(request,'mis_consultas.html',{'data':data})

def obtenerValoresApi(request, producto):
    nuevo_precio = None
    if request.method == 'POST':
        tipo_moneda = request.POST.get('tipo_moneda')
        producto_id = request.POST.get('producto_id')
        productObj = Producto.objects.get(id=producto_id)

        # Consumo de la API
        url = "mindicador.cl"
        connection = http.client.HTTPSConnection(url)
        connection.request('GET', '/api')
        response = connection.getresponse()
        
        if response.status != 200:
            return JsonResponse({'error': 'Error al conectar con la API'}, status=500)
        
        data = json.loads(response.read().decode('utf-8'))
        
        # Variables para almacenar los valores de las monedas
        dolar = data.get('dolar', {}).get('valor')
        uf = data.get('uf', {}).get('valor')
        euro = data.get('euro', {}).get('valor')
        utm = data.get('utm', {}).get('valor')

        # Verificar que los valores no sean None antes de hacer la conversión
        if tipo_moneda == 'dolar' and dolar is not None:
            nuevo_precio = round(float(producto.precio) / float(dolar), 3)  # Redondear a 3 decimales
        elif tipo_moneda == 'uf' and uf is not None:
            nuevo_precio = round(float(producto.precio) / float(uf), 3)  # Redondear a 3 decimales
        elif tipo_moneda == 'euro' and euro is not None:
            nuevo_precio = round(float(producto.precio) / float(euro), 3)  # Redondear a 3 decimales
        elif tipo_moneda == 'utm' and utm is not None:
            nuevo_precio = round(float(producto.precio) / float(utm), 3)  # Redondear a 3 decimales
        else:
            nuevo_precio = productObj.precio
        
        response_data = {'nuevo_precio': nuevo_precio}
        print("Datos de respuesta:", response_data)
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
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

def obtener_datos_api(request):

    if request.method == 'POST':
        if 'FormProducto' in request.POST:    
            url = 'https://localhost:7249/api/Producto'
            headers = {'accept': '*/*'}

            response = requests.get(url, headers=headers, verify=False) 
            if response.status_code == 200:
                datos = response.json()

                for item in datos:
                    marcaObj = Marca.objects.get(id=item['marca_id'])
                    tipoProdObj = TipoProducto.objects.get(id=item['tipoProducto_id'])     
                    Producto.objects.create(
                        nombre=item['nombre'],
                        precio=item['precio'],
                        cantidad_disponible=item['cantidad_disponible'],
                        descripcion = item['descripcion'],
                        imagen_url = item['imagen_url'],
                        marca = marcaObj,
                        tipo_producto = tipoProdObj)
            messages.success(request, 'Productos añadidos correctamente')
            messages.get_messages(request).used = True                            
        elif 'FormMarca' in request.POST:
            url = 'https://localhost:7249/api/Marcas' 
            headers = {'accept': '*/*'}

            response = requests.get(url, headers=headers, verify=False) 
            if response.status_code == 200:
                datos = response.json()

                for item in datos:
                    Marca.objects.create(
                            nombre = item['nombre']
                            )
            messages.success(request, 'Marcas añadidas correctamente')
            messages.get_messages(request).used = True          
        elif 'FormTipoProducto' in request.POST:
           url = 'https://localhost:7249/api/TipoProducto'
           headers = {'accept': '*/*'}

           response = requests.get(url, headers=headers, verify=False) 
           if response.status_code == 200:
                datos = response.json()

                for item in datos:
                    TipoProducto.objects.create(
                            nombre = item['nombre']
                            )
                messages.success(request, 'Categorias añadidas correctamente')
                messages.get_messages(request).used = True                              
    else:
        datos = ''    
    return render(request, 'getApi.html')    

def registrar_entrega(request):
    pedidos = Pedido.objects.all()
    estados = EstadoEntrega.objects.all()

    if request.method == 'POST':
        fecha = request.POST.get('fecha_entrega')
        pedido_id = request.POST.get('pedido')
        estado_entrega_id = request.POST.get('estado_entrega')

        pedido = get_object_or_404(Pedido, id=pedido_id)
        estado_entrega = get_object_or_404(EstadoEntrega, id=estado_entrega_id)

        # Verificar si ya existe una entrega para este pedido
        entrega_existente = Entrega.objects.filter(pedido=pedido).first()

        if entrega_existente:
            # Si ya existe una entrega, actualizarla en lugar de crear una nueva
            entrega_existente.fecha_entrega = fecha
            entrega_existente.estado_entrega = estado_entrega
            entrega_existente.save()
            messages.success(request, 'Entrega actualizada correctamente')
        else:
            # Si no existe una entrega, crear una nueva
            entrega_obj = Entrega(
                pedido=pedido,
                fecha_entrega=fecha,
                estado_entrega=estado_entrega
            )
            entrega_obj.save()
            messages.success(request, 'Entrega registrada correctamente')

        return redirect('index')

    return render(request, 'registrarEntrega.html', {'pedidos': pedidos, 'estados': estados})