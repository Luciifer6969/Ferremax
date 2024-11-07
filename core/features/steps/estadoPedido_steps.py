from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#Escenario Aprobar el estado del pedido desde usuario Vendedor Inicio 

@given(u'el usuario está registrado como vendedor "{correo}" "{password}"')
def step_ingresar_usuario(context,correo,password):
    wait = WebDriverWait(context.driver, 15)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Usuarios") and contains(@class, "dropdown-toggle")]')))
    menu.click()

    login_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "auth_login") and contains(@class, "dropdown-item")]')))
    login_link.click()

    wait = WebDriverWait(context.driver, 10)
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="email"]')))
    email_input.send_keys(correo)

    pwd_input = context.driver.find_element(By.XPATH, '//*[@name="password"]')
    pwd_input.send_keys(password)

    submit_button = context.driver.find_element(By.XPATH, '//*[@type="submit" and contains(text(),"Ingresar")]')
    submit_button.click()

@given(u'tiene una sesión iniciada')
def step_sesionIniciada(context):
    user_greeting = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Hola")]'))
    )
    
    # Comprueba que el texto contenga el saludo "Hola" asegurando que el usuario está autenticado
    assert user_greeting.is_displayed(), "Error: No se ha encontrado el saludo de bienvenida, el usuario no ha iniciado sesión correctamente"

@when(u'ingresa al menú de estado de pedidos')
def step_menuPedido(context):
    wait = WebDriverWait(context.driver, 15)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Estado de Pedidos") and contains(@href, "pedidos")]')))
    menu.click()

@when('selecciona el botón aprobar')
def step_botonCancelar(context):
    boton = context.driver.find_element(By.XPATH, '//*[@class="btn btn-primary shadow"][text()="Aprobar"]')
    boton.click()

@then('el sistema muestra un mensaje en pantalla indicando que el estado del pedido fue aprobado correctamente')
def step_pedidoAprobado(context):
    success_message = WebDriverWait(context.driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "alert alert-success")]'))
    )
    assert "Se Aprobó el pedido correctamente!" in success_message.text, \
        "Se Aprobó el pedido correctamente!"

#Escenario Aprobar el estado del pedido desde usuario Vendedor Fin

#Escenario Modificar estado del pedido desde usuario no registrado Inicio 

@given('el usuario no está registrado')
def step_usuarioNoRegistrado(context):
    try:
        user_greeting = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Hola")]'))
        )
        assert False, "Error: El usuario parece estar autenticado, pero debería estar sin registrar."
    except TimeoutException:
        pass


@when('intenta acceder al menú de estado de pedidos')
def step_accederMenupedido(context):
    try:
        checkMenu = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Estado de Pedidos") and contains(@href, "pedidos")]'))
        )
        assert False, "Error: El menú de 'Estado de Pedidos' es accesible para un usuario no registrado."
    except TimeoutException:
        pass

@then('el sistema no habilita el acceso al menú de estado de pedidos')
def step_sinAcceso(context):
    current_url = context.driver.current_url
    assert context.driver.current_url == current_url, "Error: La página fue redirigida, pero el usuario no debería tener acceso al menú de estado de pedidos."

#Escenario Modificar estado del pedido desde usuario no registrado Fin 

#Escenario Modificar estado del pedido desde usuario cliente registrado Inicio 

@given(u'el usuario está registrado como cliente "{correo}" "{password}"')
def step_ingresar_usuario(context,correo,password):
    wait = WebDriverWait(context.driver, 15)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Usuarios") and contains(@class, "dropdown-toggle")]')))
    menu.click()

    login_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "auth_login") and contains(@class, "dropdown-item")]')))
    login_link.click()

    wait = WebDriverWait(context.driver, 10)
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="email"]')))
    email_input.send_keys(correo)

    pwd_input = context.driver.find_element(By.XPATH, '//*[@name="password"]')
    pwd_input.send_keys(password)

    submit_button = context.driver.find_element(By.XPATH, '//*[@type="submit" and contains(text(),"Ingresar")]')
    submit_button.click()

@then('el sistema no habilita el acceso al menú de estado de pedidos por falta de permisos')
def step_menuNoHabilitado(context):
    try:
        checkMenu = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Estado de Pedidos") and contains(@href, "pedidos")]'))
        )
        assert False, "Error: El menú de 'Estado de Pedidos' es accesible para un usuario no registrado."
    except TimeoutException:
        pass

#Escenario Modificar estado del pedido desde usuario cliente registrado Fin 

#Escenario Modificar estado del pedido desde usuario Bodeguero Inicio
@given(u'el usuario está registrado como bodeguero "{correo}" "{password}"')
def step_ingresar_usuario(context,correo,password):
    wait = WebDriverWait(context.driver, 15)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Usuarios") and contains(@class, "dropdown-toggle")]')))
    menu.click()

    login_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "auth_login") and contains(@class, "dropdown-item")]')))
    login_link.click()

    wait = WebDriverWait(context.driver, 10)
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="email"]')))
    email_input.send_keys(correo)

    pwd_input = context.driver.find_element(By.XPATH, '//*[@name="password"]')
    pwd_input.send_keys(password)

    submit_button = context.driver.find_element(By.XPATH, '//*[@type="submit" and contains(text(),"Ingresar")]')
    submit_button.click()

#Escenario Modificar estado del pedido desde usuario Bodeguero Fin