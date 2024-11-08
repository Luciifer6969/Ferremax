from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

#Escenario Eliminar producto exitoso Inicio 

@when('ingresa al menú Eliminar Producto')
def step_menuEliminar(context):
    wait = WebDriverWait(context.driver, 15)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Eliminar producto") and contains(@href, "eliminar_producto")]')))
    menu.click()

@when('selecciona un producto a eliminar')
def step_selecciona_primer_producto(context):
    primer_checkbox = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '(//input[@type="checkbox" and @name="productos"])[1]'))
    )
    primer_checkbox.click()

@when('presiona el botón eliminar')
def step_presiona_primer_boton_eliminar(context):
    primer_boton_eliminar = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '(//a[contains(@class, "btn-danger") and text()="Eliminar"])[1]'))
    )
    primer_boton_eliminar.click()
    boton_confirmar_eliminar = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "swal2-confirm") and text()="Sí, eliminarlo"]'))
    )
    boton_confirmar_eliminar.click()

@then('la página se actualiza eliminando el producto y notificando al usuario El producto fue eliminado con éxito')
def step_verifica_eliminacion(context):
    mensaje_exito = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "alert alert-success") and contains(text(), "El producto fue eliminado con éxito")]'))
    )
    assert mensaje_exito.is_displayed(), "Error: No se mostró el mensaje de éxito de eliminación"

#Escenario Eliminar producto exitoso Fin 

@when('selecciona una categoría "{categoria}"')
def step_selecciona_categoria(context, categoria):
    categoria_select = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "categoria_id"))
    )
    select = Select(categoria_select)
    select.select_by_visible_text(categoria)
    
@when('presiona el botón "Eliminar categoría"')
def step_presiona_eliminar_categoria(context):
    eliminar_categoria_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='Eliminar categoria']"))
    )
    eliminar_categoria_button.click()

@then('la página se actualiza eliminando la categoría seleccionada y notificando al usuario "La categoría se ha eliminado con éxito"')
def step_verificar_eliminacion_categoria(context):
    success_message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'La categoría se ha eliminado con éxito')]"))
    )
    assert success_message is not None, "Error: No se mostró el mensaje de éxito tras eliminar la categoría"