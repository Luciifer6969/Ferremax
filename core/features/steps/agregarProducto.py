from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

#Escenario Agregar producto exitoso Inicio
@given('que un usuario bodeguero ingresó a la página FerreMax "{correo}" "{password}"')
def step_usuarioBodeguero(context,correo,password):
    context.driver.get("http://127.0.0.1:8000/")
    wait = WebDriverWait(context.driver, 15)

    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Usuarios") and contains(@class, "dropdown-toggle")]')))
    menu.click()
    login_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "auth_login") and contains(@class, "dropdown-item")]')))
    login_link.click()

    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="email"]')))
    email_input.send_keys(correo)

    pwd_input = context.driver.find_element(By.XPATH, '//*[@name="password"]')
    pwd_input.send_keys(password)

    submit_button = context.driver.find_element(By.XPATH, '//*[@type="submit" and contains(text(),"Ingresar")]')
    submit_button.click()

    user_greeting = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Hola")]'))
    )
    assert user_greeting.is_displayed(), "Error: No se ha encontrado el saludo de bienvenida, el usuario no ha iniciado sesión correctamente"


@when('accede al menú Agregar Producto')
def step_menuAgregarProducto(context):
    wait = WebDriverWait(context.driver, 15)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Agregar producto") and contains(@href, "agregar_producto")]')))
    menu.click()

@when('completa la casilla Nombre Producto "{nombreProducto}"')
def step_casillaProducto(context,nombreProducto):
    wait = WebDriverWait(context.driver, 5)
    nombre = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="nombreProducto"]')))
    nombre.send_keys(nombreProducto)

@when('completa la casilla Marca "{marca}"')
def step_casillaMarca(context,marca):
    wait = WebDriverWait(context.driver, 5)
    marcaInput = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="marcaP"]')))
    marcaInput.send_keys(marca)

@when('completa la casilla Precio "{precio}"')
def step_casillaPrecio(context,precio):
    wait = WebDriverWait(context.driver, 5)
    precioInput = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@type="number"][@name="precio"]')))
    precioInput.send_keys(precio)

@when('completa la casilla Categoría "{categoria}"')
def step_casillaCategoria(context,categoria):
    wait = WebDriverWait(context.driver, 5)
    categoriaInput = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="categoriaP"]')))
    categoriaInput.send_keys(categoria)

@when('completa la casilla Imagen "{imagen}"')
def step_casillaImagen(context,imagen):
    wait = WebDriverWait(context.driver, 5)
    imagenInput = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="imagenP"]')))
    imagenInput.send_keys(imagen)

@when('completa la casilla Descripción "{descripcion}"')
def step_casillaDescripcion(context,descripcion):
    wait = WebDriverWait(context.driver, 5)
    descripcionInput = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="descripcionProducto"]')))
    descripcionInput.send_keys(descripcion)

@when('completa la casilla Cantidad "{cantidad}"')
def step_casillaCantidad(context,cantidad):
    wait = WebDriverWait(context.driver, 5)
    cantidadInput = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@type="number"][@name="cantidad"]')))
    cantidadInput.send_keys(cantidad)

@when('presiona el botón Agregar producto')
def step_presionaBoton(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@type="submit"][text()="Agregar producto"]'))
    )
    button.click()

@then('el producto se agrega al inventario de la página y notifica al usuario que el producto fue agregado correctamente')
def step_productoAgregado(context):
    try:
        success_message = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "alert alert-success")]'))
        )
        print("HTML del mensaje:", success_message.get_attribute("outerHTML"))  # Esto imprimirá el HTML completo del elemento
        assert "Producto añadido correctamente!" in success_message.text, \
            "Error: No se mostró el mensaje de éxito después de agregar el producto."
    except TimeoutException:
        raise AssertionError("Error: No se encontró el mensaje de éxito 'alert-success' en el tiempo de espera.")
   
#Escenario Agregar producto exitoso Fin

#Escenario Agregar producto erróneo sin el nombre de producto Inicio 

@when('no completa la casilla Nombre Producto')
def step_nombreProducto(context):
    nombreCasilla = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@name="nombreProducto"]'))
    )
    nombreCasilla.clear()

@then('el producto no es agregado al inventario y notifica al usuario que falta completar el campo Nombre Producto')
def step_ProductoNoseAgrega(context):
    current_url = context.driver.current_url
    context.driver.find_element(By.XPATH, '//*[@type="submit"][text()="Agregar producto"]')
    assert context.driver.current_url == current_url, "El formulario no fue enviado debido a un error de validación"

#Escenario Agregar producto erróneo sin el nombre de producto Fin 

#Escenario Agregar producto erróneo sin la descripción del producto Inicio

@when('no completa la casilla Descripción')
def step_descripcionIncompleta(context):
    descripcionCasilla = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@name="descripcionProducto"]'))
    )
    descripcionCasilla.clear()

@then('el producto no es agregado al inventario y notifica al usuario que falta completar el campo Descripción')
def step_productoErroneo(context):
    current_url = context.driver.current_url
    context.driver.find_element(By.XPATH, '//*[@type="submit"][text()="Agregar producto"]')
    assert context.driver.current_url == current_url, "El formulario no fue enviado debido a un error de validación"
#Escenario Agregar producto erróneo sin la descripción del producto Fin

#Escenario Agregar producto exitoso sin imagen Inicio 
@when('no completa la casilla Imagen')
def step_imagenIncompleta(context):
    imagenCasilla = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@name="imagenP"]'))
    )
    imagenCasilla.clear()

@then('el producto no es agregado al inventario y notifica al usuario que falta completar el campo Imagen de producto')
def step_imagenNoseAgrega(context):
    current_url = context.driver.current_url
    context.driver.find_element(By.XPATH, '//*[@type="submit"][text()="Agregar producto"]')
    assert context.driver.current_url == current_url, "El formulario no fue enviado debido a un error de validación"

#Escenario Agregar producto exitoso sin imagen Fin

#Escenario Agregar producto erróneo sin cantidad del producto Inicio 

@when('no completa la casilla Cantidad')
def step_cantidadIncompleta(context):
    cantidadCasilla = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@type="number"][@name="cantidad"]'))
    )
    cantidadCasilla.clear()

@then('el producto no es agregado al inventario y notifica al usuario que falta completar el campo Cantidad de producto')
def step_CantidadFallida(context):
    current_url = context.driver.current_url
    context.driver.find_element(By.XPATH, '//*[@type="submit"][text()="Agregar producto"]')
    assert context.driver.current_url == current_url, "El formulario no fue enviado debido a un error de validación"

#Escenario Agregar producto erróneo sin cantidad del producto Fin

#Escenario Agregar producto erróneo sin precio del producto Inicio

@when('no completa la casilla Precio')
def step_precioIncompleto(context):
    precioCasilla = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@type="number"][@name="precio"]'))
    )
    precioCasilla.clear()

@then('el producto no es agregado al inventario y notifica al usuario que falta completar el campo Precio del producto')
def step_precioIncorrecto(context):
    current_url = context.driver.current_url
    context.driver.find_element(By.XPATH, '//*[@type="submit"][text()="Agregar producto"]')
    assert context.driver.current_url == current_url, "El formulario no fue enviado debido a un error de validación"

#Escenario Agregar producto erróneo sin precio del producto Fin

#Escenario Agregar producto erróneo sin categoría  Inicio 

@when('no completa la casilla categoría')
def step_sinCategoria(context):
    select_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "categoriaP"))
    )
    select = Select(select_element)
    select.select_by_visible_text("Selecciona una categoria")

@then('el producto no es agregado al inventario y notifica al usuario que falta completar el campo categoría del producto')
def step_categoriaFallida(context):
    try:
        # Espera que el mensaje de error sea visible en la página
        mensaje_error = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Error: Debe seleccionar una categoría válida para el producto.")]'))
        )
        # Verifica que el mensaje de error contiene el texto esperado
        assert mensaje_error.is_displayed(), "Error: El mensaje de error sobre la categoría no fue mostrado correctamente."
    except TimeoutException:
        raise AssertionError("Error: No se encontró el mensaje de error que indica que falta seleccionar una categoría.")
    

#Escenario Agregar producto erróneo sin categoría Fin

#Escenario Agregar producto erróneo sin marca Inicio 
@when('no completa la casilla Marca')
def step_sinMarca(context):
    select_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "marcaP"))
    )
    select = Select(select_element)
    select.select_by_visible_text("Selecciona una marca")

@then('el producto no es agregado al inventario y notifica al usuario que falta completar el campo Marca del producto')
def step_marcaFallida(context):
    try:
        # Espera que el mensaje de error sea visible en la página
        mensaje_error = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Error: Debe seleccionar una marca válida para el producto.")]'))
        )
        # Verifica que el mensaje de error contiene el texto esperado
        assert mensaje_error.is_displayed(), "Error: El mensaje de error sobre la marca no fue mostrado correctamente."
    except TimeoutException:
        raise AssertionError("Error: No se encontró el mensaje de error que indica que falta seleccionar una marca.")
#Escenario Agregar producto erróneo sin marca Fin

#Escenario Redirección del botón Cancelar Inicio 
@then('el usuario es redirigido a la página principal de FerreMax')
def step_redirigidoPaginaPrincipal(context):
    # Espera a que la URL actual coincida con la URL esperada
    WebDriverWait(context.driver, 10).until(
        lambda driver: driver.current_url == "http://127.0.0.1:8000/"
    )
    
    # Verifica que la URL actual es la página principal
    assert context.driver.current_url == "http://127.0.0.1:8000/", \
        f"Error: La URL actual '{context.driver.current_url}' no es la página principal esperada."
    
#Escenario Redirección del botón Cancelar Fin 


#Escenario Ingreso de caracteres especiales en formulario agregar producto Inicio
@then('el sistema no agrega el producto y notifica al usuario que no se acepta caracteres especiales')
def step_caracteresEspeciales(context):
    try:
        # Espera hasta que el mensaje de error de caracteres especiales aparezca en pantalla
        error_message = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "alert alert-danger")]'))
        )
        # Verifica que el mensaje de error contiene el texto esperado
        assert "Error: No se acepta caracteres especiales en los campos del producto" in error_message.text, \
            f"Error: Se esperaba un mensaje de caracteres especiales, pero se encontró: '{error_message.text}'"
    except TimeoutException:
        raise AssertionError("Error: El mensaje de advertencia de caracteres especiales no se encontró en el tiempo de espera.")

#Escenario Ingreso de caracteres especiales en formulario agregar producto Fin

#Escenario Ingresar un producto con valor negativo en precio de producto Inicio

@then('el producto no es agregado al inventario y notifica al usuario que el precio debe ser mayor a 0')
def step_numeroNegativo(context):
    try:
        # Espera hasta que el span de error del precio esté visible
        error_precio_span = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="pPrecioId" and contains(text(), "El valor no puede ser menor a 0")]'))
        )
        
        # Verifica que el mensaje en el span sea el esperado
        assert error_precio_span.text == "El valor no puede ser menor a 0", \
            f"Error: El mensaje encontrado fue '{error_precio_span.text}', se esperaba 'El valor no puede ser menor a 0'."
    
    except TimeoutException:
        raise AssertionError("Error: No se encontró el mensaje de validación para el precio.")


#Escenario Ingresar un producto con valor negativo en precio de producto Fin

#Escenario Ingresar un producto con valor negativo en cantidad de producto Inicio

@then('el producto no es agregado al inventario y notifica al usuario que la cantidad debe ser mayor a 0')
def step_cantidadNegativa(context):
    try:
        # Espera hasta que el span de error del precio esté visible
        error_cantidad_span = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//span[@id="pCantidadId" and contains(text(), "El valor no puede ser menor a 0")]'))
        )
        
        # Verifica que el mensaje en el span sea el esperado
        assert error_cantidad_span.text == "El valor no puede ser menor a 0", \
            f"Error: El mensaje encontrado fue '{error_cantidad_span.text}', se esperaba 'El valor no puede ser menor a 0'."
    
    except TimeoutException:
        raise AssertionError("Error: No se encontró el mensaje de validación para la cantidad.")


#Escenario Ingresar un producto con valor negativo en cantidad de producto Fin