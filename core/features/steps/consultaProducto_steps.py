from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


#Escenario Consulta de producto exitosa Inicio

@when('tiene una sesión iniciada')
def verificar_sesion_iniciada(context):
    try:
        # Esperar que aparezca un elemento que solo esté visible cuando el usuario esté logueado.
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Hola")]'))
        )
    except TimeoutException:
        assert False, "La sesión no se inició correctamente, el elemento 'Cerrar sesión' no está presente"

@when(u'ingresa al menú de consulta')
def opcionConsulta(context):
    wait = WebDriverWait(context.driver, 15)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Consultas") and contains(@class, "dropdown-toggle")]')))
    menu.click()

@when(u'ingresa a la opción Consultar producto')
def opcionConsulta(context):
    wait = WebDriverWait(context.driver, 15)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/contact/" and contains(@class, "dropdown-item")]')))
    menu.click()


@when(u'ingresa un motivo de consulta "{motivo}"')
def opcionMotivo(context,motivo):
    motivo_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@name="motivo" and @type="text"]'))
    )
    motivo_input.send_keys(motivo)

@when(u'selecciona un producto de la lista "{producto}"')
def selecciona_producto(context, producto):
    select_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "productoId"))
    )
    select = Select(select_element)
    
    select.select_by_visible_text(producto)

@when('completa la casilla de comentarios "{comentario}"')
def opcionComentario(context,comentario):
    comentario_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@name="comment"]'))
    )
    comentario_input.send_keys(comentario)

@when('presiona el botón Enviar comentario')
def step_presiona_boton_enviarComentario(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@type="submit"][text()="Enviar comentario"]'))
    )
    button.click()

@then('se envía la consulta con éxito')
def step_consultaExitosa(context):
    success_message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "alert alert-success")]'))
    )
    assert "Registro añadido correctamente" in success_message.text, \
        "Registro añadido correctamente"

#Escenario Consulta de producto exitosa Fin

#Escenario Consulta de producto erróneo sin selección de producto  Inicio

@when('no selecciona un producto del inventario')
def step_sinProducto(context):
    select_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "productoId"))
    )
    select = Select(select_element)
    select.select_by_visible_text("Seleccion un producto")

@then('no se envía la consulta con éxito y se notifica al usuario que no se puede realizar la consulta')
def step_consultaProductoInvalido(context):
    error_message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "alert alert-danger")]'))
    )
    assert "Por favor, selecciona un producto antes de enviar el formulario." in error_message.text, \
        "Por favor, selecciona un producto antes de enviar el formulario."
    
#Escenario Consulta de producto erróneo sin selección de producto  Fin

#Escenario Consulta de producto erróneo sin motivo de consulta Inicio 
@when('deja vacía la casilla Motivo de consulta')
def step_consultaSinMotivo(context):
    motivoInput = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@name="motivo" and @type="text"]'))
    )
    motivoInput.clear()

@then('no se envía la consulta con éxito y se notifica al usuario que no se puede realizar la consulta sin motivo')
def step_consultaSinMotivo(context):
    current_url = context.driver.current_url
    context.driver.find_element(By.XPATH, '//*[@type="submit"][text()="Enviar comentario"]')
    assert context.driver.current_url == current_url, "El formulario no fue enviado debido a un error de validación"

#Escenario Consulta de producto erróneo sin motivo de consulta Fin

#Escenario Consulta de producto erróneo sin comentario Inicio 
@when('deja la casilla comentario vacía')
def step_consultaSinMotivo(context):
    comentarioInput = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@name="motivo" and @type="text"]'))
    )
    comentarioInput.clear()

@then('el sistema muestra un mensaje señalando que la casilla comentario es obligatoria')
def step_consultaSinComentario(context):
    current_url = context.driver.current_url
    context.driver.find_element(By.XPATH, '//*[@type="submit"][text()="Enviar comentario"]')
    assert context.driver.current_url == current_url, "El formulario no fue enviado debido a un error de validación"

#Escenario Consulta de producto erróneo sin comentario Fin
