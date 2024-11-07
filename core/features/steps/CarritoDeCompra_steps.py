from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

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
def step_verificaCantidad(context):
    cart_quantity = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'cart_quantity'))
    )
    
    quantity_text = cart_quantity.text.strip()
    assert quantity_text.isdigit() and int(quantity_text) > 0, f"Error: El carrito muestra una cantidad inválida o cero productos (valor actual: '{quantity_text}')"

#Escenario Agregar producto Fin

#Escenario Modificar cantidad del producto en el carrito de compra Inicio

@given('tiene productos agregados al carrito')
def step_agregaProducto(context):
    step_menuProducto(context)
    step_elige_producto(context)
    step_agregar_al_carrito(context)
    step_verificaCantidad(context)

@given('ingresa al menú Carrito de compra')
def step_ingresaAlCarro(context):
    wait = WebDriverWait(context.driver, 20)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "cart")]')))
    menu.click()

@when('selecciona una cantidad de producto')
def step_seleccionaCantidad(context):
    wait = WebDriverWait(context.driver, 10)
    cantidad_select = wait.until(EC.visibility_of_element_located((By.ID, 'select1')))
    select = Select(cantidad_select)
    select.select_by_value("1") 

@when('selecciona el botón Agregar cantidad')
def step_agregaCantidad(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@type="button" and text()="Agregar Cantidad"]'))
    )
    button.click()

@then('se modifica la cantidad de producto')
def step_cantidadModificada(context):
    cantidad_display = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//p[strong[contains(text(), "Cantidad:")]]'))
    )
    cantidad_text = cantidad_display.text.strip()
    cantidad_actual = int(cantidad_text.split(":")[1].strip())
    assert cantidad_actual >= 1, f"Error: La cantidad de producto no se modificó correctamente, valor actual: {cantidad_actual}"

#Escenario Modificar cantidad del producto en el carrito de compra Fin


#Escenario Eliminar producto del carrito de compra Inicio 
@given('presiona el botón Eliminar producto')
def step_elminarProducto(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@type="button" and text()="Eliminar Producto"]'))
    )
    button.click()

@then('el producto es eliminado del carrito')
def step_productoRemovidoDelCarro(context):
    try:
        # Espera a que aparezca cualquiera de los elementos que indica que el carrito está vacío
        mensaje_carro_vacio = WebDriverWait(context.driver, 15).until(
            EC.presence_of_element_located((
                By.XPATH,
                '//div[@class="card text-center"]//div[contains(text(), "No se encuentran productos en el carro")] | \
                 //div[@class="card text-center"]//p[contains(text(), "Tu carro de compra se encuentra vacio!")] | \
                 //div[@class="card text-center"]//img[@alt="Imagen de no hay productos"]'
            ))
        )
        
        # Verifica que el elemento fue encontrado (cualquiera de los mensajes o la imagen)
        assert mensaje_carro_vacio is not None, "Error: No se encontró el mensaje de carrito vacío."
        
    except TimeoutException:
        raise AssertionError("Error: No se encontró el mensaje o indicador de carrito vacío en el tiempo de espera.")
#Escenario Eliminar producto del carrito de compra Fin
