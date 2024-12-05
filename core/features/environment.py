from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os, time
from datetime import datetime

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

def after_step(context, step):
    """
    Captura una captura de pantalla después de cada paso.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")

    # Crea el directorio si no existe
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    # Genera el archivo de captura con el nombre del paso
    screenshot_path = os.path.join(screenshots_dir, f"{step.name}_{timestamp}.png")

    # Esperar un momento para asegurar que la página esté estable
    time.sleep(1)  # Agrega un pequeño retraso de 1 segundo

    # Captura la pantalla
    context.driver.save_screenshot(screenshot_path)
    print(f"Captura de pantalla guardada en: {screenshot_path}")