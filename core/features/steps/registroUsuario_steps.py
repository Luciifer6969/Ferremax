from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from inicioSesion_steps import abrir_explorador

# Escenario Registro de usuario exitoso Inicio

@when(u'accede a la opción de Registrarse')
def opcionRegistrar(context):
    wait = WebDriverWait(context.driver, 15)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Usuarios") and contains(@class, "dropdown-toggle")]')))
    menu.click()
    register = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "auth_register") and contains(@class, "dropdown-item")]')))
    register.click()
# Escenario Registro de usuario exitoso Fin


