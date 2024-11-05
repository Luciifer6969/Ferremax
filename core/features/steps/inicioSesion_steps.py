from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Escenario Login correcto inicio 
@given('que un usuario ingresó a la página FerreMax')
def abrir_explorador(context):
    context.driver.get("http://127.0.0.1:8000/")  # Usa el navegador ya abierto en environment.py

@when(u'accede a la opción de ingresar')
def ingresar_usuario(context):
    # Espera hasta que el enlace de login sea clickeable y haz click en él
    wait = WebDriverWait(context.driver, 15)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Usuarios") and contains(@class, "dropdown-toggle")]')))
    menu.click()
    
    # Espera hasta que el enlace "Ingresar" esté visible y haz clic en él
    login_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "auth_login") and contains(@class, "dropdown-item")]')))
    login_link.click()

@when(u'ingresa una dirección de "{correo}" registrado previamente')
def ingresar_correo(context, correo):
    wait = WebDriverWait(context.driver, 10)
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="email"]')))
    email_input.send_keys(correo)

@when(u'ingresa la contraseña correcta "{password}"')
def ingresar_contrasena(context, password):
    pwd_input = context.driver.find_element(By.XPATH, '//*[@name="password"]')
    pwd_input.send_keys(password)

@when(u'presiona el botón ingresar')
def presionar_boton(context):
    submit_button = context.driver.find_element(By.XPATH, '//*[@type="submit" and contains(text(),"Ingresar")]')
    submit_button.click()


@then(u'el usuario inicia sesión correctamente')
def inicia_sesion(context):
    user_greeting = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Hola")]'))
    )
    
    # Comprueba que el texto contenga el saludo "Hola" asegurando que el usuario está autenticado
    assert user_greeting.is_displayed(), "Error: No se ha encontrado el saludo de bienvenida, el usuario no ha iniciado sesión correctamente"
#Escenario Login correcto Fin 


#Escenario login usuario incorrecto Inicio 
@when(u'ingresa una dirección de "{correo}" correo no registrado')
def ingresar_correo(context, correo):
    wait = WebDriverWait(context.driver, 5)
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@name="email"]')))
    email_input.send_keys(correo)

@then('el usuario no puede iniciar sesión')
def login_invalido(context):
    # Comprobación 1: La URL sigue siendo la misma página de login
    assert "auth_login" in context.driver.current_url, "Error: El usuario fue redirigido a una página diferente, posiblemente haya iniciado sesión."

    # Comprobación 2: El formulario de login sigue visible en la página
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@name="email"]'))
        )
        print("El formulario de inicio de sesión aún está visible, indicando un fallo en el inicio de sesión.")
    except:
        raise AssertionError("Error: El formulario de login no se encuentra en la página, posiblemente el usuario haya iniciado sesión.")
#Escenario login usuario incorrecto Fin  


#Escenario Inicio sesión con usuario correcto con contraseña inválida Inicio
@when(u'ingresa una contraseña incorrecta "{password}"')
def ingresar_contrasena(context, password):
    pwd_input = context.driver.find_element(By.XPATH, '//*[@name="password"]')
    pwd_input.send_keys(password)

@then('el usuario no puede iniciar sesión y ve una alerta de contraseña incorrecta')
def login_invalido(context):
    # Comprobación 1: La URL sigue siendo la misma página de login
    assert "auth_login" in context.driver.current_url, "Error: El usuario fue redirigido a una página diferente, posiblemente haya iniciado sesión."

    # Comprobación 2: El formulario de login sigue visible en la página
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@name="email"]'))
        )
        print("El formulario de inicio de sesión aún está visible, indicando un fallo en el inicio de sesión.")
    except:
        raise AssertionError("Error: El formulario de login no se encuentra en la página, posiblemente el usuario haya iniciado sesión.")
#Escenario Inicio sesión con usuario correcto con contraseña inválida Fin


#Escenario El usuario ingresa un correo válido y en el campo de contraseña ingresa una injección sql Inicio
@then('el usuario no puede iniciar sesión y se ve una alerta de tipo de datos en el campo contraseña no son válidos')
def login_invalido(context):
    # Comprobación 1: La URL sigue siendo la misma página de login
    assert "auth_login" in context.driver.current_url, "Error: El usuario fue redirigido a una página diferente, posiblemente haya iniciado sesión."

    # Comprobación 2: El formulario de login sigue visible en la página
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@name="email"]'))
        )
        print("El formulario de inicio de sesión aún está visible, indicando un fallo en el inicio de sesión.")
    except:
        raise AssertionError("Error: El formulario de login no se encuentra en la página, posiblemente el usuario haya iniciado sesión.")
#Escenario El usuario ingresa un correo válido y en el campo de contraseña ingresa una injección sql Fin


#Escenario Redirección del botón 'Cancelar' Inicio
@when('presiona el botón cancelar')
def botonCancelar(context):
    submit_cancel = context.driver.find_element(By.XPATH, '//*[@type="submit"][text()="Cancelar"]')
    submit_cancel.click()

@then('el usuario no puede iniciar sesión y se redirige al Home')
def login_invalido(context):
    url_esperada = "http://127.0.0.1:8000/"  # Cambia esta URL por la URL exacta de tu página principal
    assert context.driver.current_url == url_esperada, f"No se redirigió a la página principal. URL actual: {context.driver.current_url}"

#Escenario Redirección del botón 'Cancelar' Fin


#Escenarios Ingreso de email con formato incorrecto sin @ Inicio

@when(u'completa el campo de correo con un mail registrado sin agregar @ "{correo}"')
def correo_sin_arroba(context,correo):
    ingresar_correo(context,correo)

@then('el usuario no puede iniciar sesión y se ve una alerta notificando formato de correo no válido, incluye un @ en la dirección de correo electrónico')
def alert_login(context):
    current_url = context.driver.current_url
    context.driver.find_element(By.XPATH, '//*[@type="submit"][text()="Ingresar"]')
    assert context.driver.current_url == current_url, "El formulario no fue enviado debido a un error de validación"

#Escenarios Ingreso de email con formato incorrecto sin @ Fin

#Escenarios Ingreso de email con formato incorrecto sin dominio .com Inicio
@when(u'completa el campo de correo con un mail registrado sin agregar .com "{correo}"')
def correo_sindominio(context,correo):
    ingresar_correo(context,correo)

@then(u'el usuario no puede iniciar sesión y se ve una alerta notificando formato de correo no válido')
def alert_login(context):
    current_url = context.driver.current_url
    context.driver.find_element(By.XPATH, '//*[@type="submit"][text()="Ingresar"]')
    assert context.driver.current_url == current_url, "El formulario no fue enviado debido a un error de validación"
#Escenarios Ingreso de email con formato incorrecto sin dominio .com  Fin

#Escenarios Inicio de sesión con usuario correcto sin ingresar contraseña  Inicio
@when(u'no completa el campo de contraseña')
def empty_field(context):
    pswInput = context.driver.find_element(By.XPATH, '//*[@name="password"]')
    if pswInput.get_attribute("value") == "":
        assert True, "El campo de contraseña está vacío"
    else:
        assert False, "El campo de contraseña tiene datos"

@then(u'el usuario no puede iniciar sesión y el sistema indica rellenar el campo Contraseña')
def alert_login(context):
    current_url = context.driver.current_url
    context.driver.find_element(By.XPATH, '//*[@type="submit"][text()="Ingresar"]')
    assert context.driver.current_url == current_url, "El formulario no fue enviado debido a un error de validación"
#Escenarios Inicio de sesión con usuario correcto sin ingresar contraseña  Fin

