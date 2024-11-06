from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Escenario Registro de usuario exitoso Inicio

@when(u'accede a la opción de Registrarse')
def opcionRegistrar(context):
    wait = WebDriverWait(context.driver, 15)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Usuarios") and contains(@class, "dropdown-toggle")]')))
    menu.click()
    register = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "auth_register") and contains(@class, "dropdown-item")]')))
    register.click()

@when('completa el campo Nombre Usuario "{username}"')
def step_completa_username(context, username):
    username_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@name='username']"))
    )
    username_input.send_keys(username)

@when('completa el campo Nombre "{name}"')
def step_completa_name(context, name):
    name_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@name='name']"))
    )
    name_input.send_keys(name)

@when('completa el campo Apellido "{surname}"')
def step_completa_surname(context, surname):
    surname_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@name='last_name']"))
    )
    surname_input.send_keys(surname)

@when('completa el campo Correo electrónico "{email}"')
def step_completa_email(context, email):
    email_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@type='email'][@name='email']"))
    )
    email_input.send_keys(email)

@when('completa el campo Confirme correo electrónico "{email2}"')
def step_completa_email2(context, email2):
    email2_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@type='email2'][@name='email2']"))
    )
    email2_input.send_keys(email2)

@when('completa el campo Contraseña "{password}"')
def step_completa_password(context, password):
    password_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@type='password'][@name='password']"))
    )
    password_input.send_keys(password)

@when('completa el campo Confirme contraseña "{password2}"')
def step_completa_password2(context, password2):
    password2_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@type="password"][@name="password2"]'))
    )
    password2_input.send_keys(password2)

@when('presiona el boton Registrarse')
def step_presiona_registrar(context):
    registrar_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@type="submit"][text()="Registrarse"]'))
    )
    registrar_button.click()

@then('el sistema registra el usuario y se redige al menú principal')
def step_verifica_registro_exitoso(context):
    # Espera hasta que se redirija a la página principal y verifica el título
    WebDriverWait(context.driver, 10).until(EC.url_contains("http://127.0.0.1:8000/"))
    assert "Menu Principal" in context.driver.title, "El registro no fue exitoso o no se redirigió correctamente"
# Escenario Registro de usuario exitoso Fin

#Escenario Registro de usuario erróneo sin nombre de usuario Inicio 
@when('deja vacío el campo Nombre Usuario')
def step_deja_vacio_username(context):
    username_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@name='username']"))
    )
    username_input.clear()
@then('el sistema no permite el registro y notifica que hay un campo incompleto en el formulario')
def step_registroInvalido(context):
    current_url = context.driver.current_url
    context.driver.find_element(By.XPATH, '//*[@type="submit"][text()="Registrarse"]')
    assert context.driver.current_url == current_url, "El formulario no fue enviado debido a un error de validación"
#Escenario Registro de usuario erróneo sin nombre de usuario Fin

#Escenario Registro de usuario erróneo sin nombre  Inicio 
@when('deja vacío el campo Nombre')
def step_deja_vacio_nombre(context):
    name_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@name='name']"))
    )
    name_input.clear()
#Escenario Registro de usuario erróneo sin nombre  Fin

#Escenario Registro de usuario erróneo con correos electronicos diferentes  Inicio 
@when('completa el campo Confirme correo electrónico con un correo diferente "{email}"')
def step_completa_email_incorrecto(context, email):
    email_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@name="email2"]'))
    )
    email_input.send_keys(email)

@then('el sistema no permite el registro y notifica que los campos Correo electrónico y Confirme correo electrónico no coinciden')
def step_correo_sin_coincidencia(context):
    error_message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "alert alert-danger")]'))
    )
    assert "Error en el registro. Por favor, corrija los campos resaltados." in error_message.text, \
        "El mensaje de error no se mostró como se esperaba"

#Escenario Registro de usuario erróneo con correos electronicos diferentes  Fin