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

@when(u'selecciona un producto del inventario "{producto}"')
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