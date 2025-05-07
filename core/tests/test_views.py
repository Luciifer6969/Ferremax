import pytest 
from core.models import Producto, Marca, TipoProducto, Contact
from django.contrib.auth.models import User

@pytest.mark.django_db
#Caso de uso R.F. 6 001 Conversion de moneda del producto a dolar INICIO

def test_obtener_valores_api_dolar(client):
    # crear marca object
    marcaObj = Marca.objects.create(nombre="Marcatest")

    # crear tipo_producto object
    tipo_productoObj = TipoProducto.objects.create(nombre="TipoTest")

    # crear Producto object
    producto = Producto.objects.create(nombre="Producto Test",marca=marcaObj,tipo_producto=tipo_productoObj,precio=100.0,cantidad_disponible=10, descripcion="Descripcion Test", imagen_url="https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg")

    # Check if the product exists   
    assert producto is not None, "Producto no encontrado"

    # Prepare POST data
    post_data = {
        "tipo_moneda": "dolar",
        "producto_id": producto.id,
    }
    # Hacer POST a la URL correspondiente
    response = client.post(f"/producto/{producto.id}/", post_data)

    # Verificar la respuesta
    assert response.status_code == 200
    # Decodificar el contenido HTML
    html_content = response.content.decode('utf-8')
    assert "Producto Test" in html_content

    nuevo_precio_calculado = round(producto.precio / 1.0, 3)  # Ajusta el divisor según el valor esperado de la API
    assert str(nuevo_precio_calculado) in html_content

#Caso de uso R.F. 6 001 Conversion de moneda del producto a dolar FIN

#Caso de uso R.F. 6 002 Conversion de moneda del producto a euro INICIO

@pytest.mark.django_db
def test_obtener_valores_api_euro(client):
    # crear marca object
    marcaObj = Marca.objects.create(nombre="Marcatest")

    # crear tipo_producto object
    tipo_productoObj = TipoProducto.objects.create(nombre="TipoTest")

    # crear Producto object
    producto = Producto.objects.create(nombre="Producto Test",marca=marcaObj,tipo_producto=tipo_productoObj,precio=100.0,cantidad_disponible=10, descripcion="Descripcion Test", imagen_url="https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg")

    # Check if the product exists   
    assert producto is not None, "Producto no encontrado"

    # Prepare POST data
    post_data = {
        "tipo_moneda": "euro",
        "producto_id": producto.id,
    }
    # Hacer POST a la URL correspondiente
    response = client.post(f"/producto/{producto.id}/", post_data)

    # Verificar la respuesta
    assert response.status_code == 200
    # Decodificar el contenido HTML
    html_content = response.content.decode('utf-8')
    assert "Producto Test" in html_content

    nuevo_precio_calculado = round(producto.precio / 1.0, 3)
    # Ajusta el divisor según el valor esperado de la API
    assert str(nuevo_precio_calculado) in html_content

#Caso de uso R.F. 6 002 Conversion de moneda del producto a euro FIN

#Caso de uso R.F.7 001 Agregar un producto al sistema INICIO 

@pytest.mark.django_db
def test_agregar_producto(client):
    # crear marca object
    marcaObj = Marca.objects.create(nombre="Marcatest")

    # crear tipo_producto object
    tipo_productoObj = TipoProducto.objects.create(nombre="TipoTest")

    # crear Producto object
    producto = Producto.objects.create(nombre="Producto Test",marca=marcaObj,tipo_producto=tipo_productoObj,precio=100.0,cantidad_disponible=10, descripcion="Descripcion Test", imagen_url="https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg")

    # Check if the product exists   
    assert producto is not None, "Producto no encontrado"

    # Prepare POST data
    post_data = {
        "nombre": "Nuevo Producto",
        "descripcion": "Descripcion del nuevo producto",
        "precio": 50.0,
        "cantidad_disponible": 20,
        "marca": marcaObj.id,
        "tipo_producto": tipo_productoObj.id,
        "imagen_url": "https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg"
    }
    
    # Hacer POST a la URL correspondiente
    response = client.post("/agregar_producto/", post_data)

    # Verificar la respuesta
    assert response.status_code == 200


#Caso de uso R.F.7 001 Agregar un producto al sistema FIN

#Caso de uso R.F.7 002 Actualizar un dato de un producto ya registrado INICIO

@pytest.mark.django_db
def test_actualizar_producto(client):
    # crear marca object
    marcaObj = Marca.objects.create(nombre="Marcatest")

    # crear tipo_producto object
    tipo_productoObj = TipoProducto.objects.create(nombre="TipoTest")

    # crear Producto object 
    producto = Producto.objects.create(nombre="Producto Test",
                                       marca=marcaObj,
                                       tipo_producto=tipo_productoObj,
                                       precio=100.0,
                                       cantidad_disponible=10,
                                       descripcion="Descripcion Test", 
                                       imagen_url="https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg")

    # Check if the product exists   
    assert producto is not None, "Producto no encontrado"

    # Prepare POST data
    post_data = {
        "nombreProducto": "Producto Actualizado",
        "descripcionProducto": "Descripcion actualizada",
        "precio": 1500,
        "cantidad": 15,
        "marcaP": marcaObj.id,
        "categoriaP": tipo_productoObj.id,
        "imagenP": "https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg"
    }
    
    # Hacer POST a la URL correspondiente
    response = client.post(f"/editar_producto/{producto.id}/", post_data)

    # Verificar la respuesta
    assert response.status_code == 302  # Redirección esperada después de la actualización
    # Verificar que el producto se haya actualizado correctamente  
    assert Producto.objects.filter(id=producto.id, nombre="Producto Actualizado").exists(), "El producto no se actualizó correctamente"


#Caso de uso R.F.7 002 Actualizar un dato de un producto ya registrado FIN

#Caso de uso R.F.8 001 Agregar una consulta de producto exitosa INICIO


@pytest.mark.django_db
def test_agregar_consulta_producto(client):
    # crear marca object
    marcaObj = Marca.objects.create(nombre="Marcatest")
    # crear tipo_producto object
    TipoProductoObj = TipoProducto.objects.create(nombre="TipoTest")

    # Crear producto object
    productoObj = Producto.objects.create(nombre="Producto Test",
                                       marca=marcaObj,
                                       tipo_producto=TipoProductoObj,
                                       precio=100.0,
                                       cantidad_disponible=10,
                                       descripcion="Descripcion Test",
                                       imagen_url="https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg")

    # Crear usuario object
    usuarioObj = User.objects.create_user(username="testuser", password="testpassword")

    # Autenticar el usuario
    client.login(username="testuser", password="testpassword")

    #Post data para la consulta
    post_data = {
        "motivo": "Prueba de motivo de producto",
        "comment": "Prueba de producto",
        "productoId": productoObj.id,
        "usuario": usuarioObj.id
    }

    # Hacer POST a la URL correspondiente
    response = client.post("/contact/", post_data)
    assert response.status_code == 302 # Verificar que la respuesta sea exitosa (200 OK)
    # Verificar que la consulta se haya guardado correctamente
    assert Contact.objects.filter(motivo="Prueba de motivo de producto", comentario="Prueba de producto").exists(), "La consulta no se guardó correctamente"
    # Verificar que el producto y el usuario existan
    assert Producto.objects.filter(id=productoObj.id).exists(), "El producto no existe"
    assert User.objects.filter(id=usuarioObj.id).exists(), "El usuario no existe"
    
#Caso de uso R.F.8 001 Agregar una consulta de producto exitosa FIN