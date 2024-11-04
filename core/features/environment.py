from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def before_all(context):
    context.driver = webdriver.Chrome() 
    context.driver.maximize_window() 
    
def after_all(context):
    context.driver.quit()

#funcion para cerrar sesion despues de cada escenario
def after_scenario(context, Scenario):
    # Intentar cerrar sesión si el usuario está autenticado
    try:
        wait = WebDriverWait(context.driver, 15)
        menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Hola") and contains(@class, "dropdown-toggle")]')))
        menu.click()
        logout_link = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "logout")]'))
        )
        logout_link.click()
        print("Sesión cerrada correctamente.")
    except:
        # Si no se encuentra el enlace de cierre de sesión, asume que no hay sesión iniciada y continúa
        print("Error al cerrar sesión:")
        pass
