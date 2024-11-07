from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#Escenario Agregar producto Inicio
@when('ingresa al menú de productos')
def step_menuProducto(context):
    wait = WebDriverWait(context.driver, 15)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Productos") and contains(@href, "productos")]')))
    menu.click()

@when('elige un producto del menú')
def step_elige_producto(context):
    wait = WebDriverWait(context.driver, 10)
    producto = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "card")]')))
    context.selected_product = producto

@when('presiona el botón Agregar al carrito en el producto deseado')
def step_agregar_al_carrito(context):
    agregar_button = context.selected_product.find_element(By.XPATH, './/button[contains(@class, "agregar-carrito") and contains(text(), "Agregar al carrito")]')
    agregar_button.click()

@then('el producto es agregado al carrito de compras de la página')
def step_productoAgregado(context):
    cart_quantity = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'cart_quantity'))
    )
    
    quantity_text = cart_quantity.text.strip()
    assert quantity_text.isdigit() and int(quantity_text) > 0, f"Error: El carrito muestra una cantidad inválida o cero productos (valor actual: '{quantity_text}')"

#Escenario Agregar producto Fin

