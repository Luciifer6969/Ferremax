from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@when('se dirige a iniciar sesión')
def step_navigate_to_login(context):
    try:
        # Utilizando el nuevo xpath para "Usuarios" e "Ingresar"
        usuarios_link = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarSupportedContent"]/ul[2]/li[2]/a'))
        )
        usuarios_link.click()
        
        ingresar_link = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarSupportedContent"]/ul[2]/li[2]/ul/li[1]/a'))
        )
        ingresar_link.click()
    except TimeoutException:
        print("Error: No se encontró el enlace de inicio de sesión.")

@when('el usuario está registrado como bodeguero "{email}" "{password}"')
def step_login_as_bodeguero(context, email, password):
    email_field = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@name='email']"))
    )
    email_field.clear()
    email_field.send_keys(email)
    
    password_field = context.driver.find_element(By.XPATH, "//*[@name='password']")
    password_field.clear()
    password_field.send_keys(password)
    
    login_button = context.driver.find_element(By.XPATH, "//*[@type='submit'][text()='Ingresar']")
    login_button.click()

@when('el usuario tiene una sesión iniciada')
def step_session_is_active(context):
    pass  # Este paso se asume cumplido si el inicio de sesión fue exitoso

@when('presiona el botón "Menu Actualizar "')
def step_click_update_product_button(context):
    actualizar_producto_link = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*//*[@id="navbarSupportedContent"]/ul[1]/a'))
    )
    actualizar_producto_link.click()

@when('selecciona un producto para actualizar')
def step_select_product_to_update(context):
    producto_para_actualizar = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/main/table/tbody/tr[1]/td[9]/a"))
    )
    producto_para_actualizar.click()

@when('cambia el nombre del producto a través del formulario')
def step_clear_product_name(context):
    nombre_producto_field = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="nombreProducto"]'))
    )
    nombre_producto_field.clear()

@when('cambia el nombre del producto "{nombre}"')
def step_set_product_name(context, nombre):
    nombre_producto_field = context.driver.find_element(By.XPATH, '//*[@id="nombreProducto"]')
    nombre_producto_field.send_keys(nombre)

@when('presiona el botón "Actualizar producto" después de hacer cambios')
def step_click_save_changes_button(context):
    actualizar_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[2]/form/div[8]/button"))
    )
    actualizar_button.click()

@then('el sistema actualiza el producto y notifica al usuario que el producto se actualizó con éxito')
def step_verify_product_updated_successfully(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'producto se actualizó con éxito')]"))
    )
    context.driver.quit()
