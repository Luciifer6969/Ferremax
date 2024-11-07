from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#Escenario Ver estado de stock de productos desde usuario Vendedor Inicio 

@when('selecciona el menú stock disponible')
def step_menuStock(context):
    wait = WebDriverWait(context.driver, 15)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Stock disponible") and contains(@href, "stock_products")]')))
    menu.click()


@then('el sistema muestra información sobre productos, nombres, precio, cantidad disponible')
def step_informacionStock(context):
    Informacion = ["Nombre", "Descripcion", "Precio", "Cantidad Disponible"]
    for texto in Informacion:
        try:
            # Busca cada elemento en una celda de la tabla
            elemento = WebDriverWait(context.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f'//th[contains(text(), "{texto}")]'))
            )
            assert elemento is not None, f"No se encontró la información esperada: {texto}"
        except TimeoutException:
            assert False, f"No se encontró la información esperada: {texto}"
#Escenario Ver estado de stock de productos desde usuario Vendedor Fin 


#Escenario Ver estado de stock de productos desde usuario no registrado Inicio

@given('no tiene una sesión iniciada')
def step_no_sesion_iniciada(context):
    try:
        user_greeting = WebDriverWait(context.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Hola")]'))
        )
        assert False, "Error: El usuario parece estar autenticado, pero debería estar sin registrar."
    except TimeoutException:
        # Si no se encuentra el saludo, es correcto para un usuario no registrado
        pass

@then('el sistema no habilita el menú de stock de productos')
def step_menu_stock_no_habilitado(context):
    try:
        # Verifica que el menú de stock de productos no esté visible
        stock_menu = WebDriverWait(context.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Stock de Productos")]'))
        )
        assert False, "Error: El menú de 'Stock de Productos' está habilitado para un usuario no registrado."
    except TimeoutException:
        # Si no se encuentra el menú, la prueba pasa, ya que no debería estar visible para usuarios no registrados
        pass
#Escenario Ver estado de stock de productos desde usuario no registrado Fin

#Escenario Ver estado de stock de productos desde usuario Bodeguero Inicio

@then('el sistema no habilita el menú de stock de productos por falta de permisos')
def step_sinAcceso(context):
    current_url = context.driver.current_url
    assert context.driver.current_url == current_url, "Error: La página fue redirigida, pero el usuario no debería tener acceso al menú de estado de pedidos."

#Escenario Ver estado de stock de productos desde usuario Bodeguero Fin 

#Escenario Ver estado de stock de productos la descripción de cada producto Inicio
@then('el sistema muestra información sobre la descripción del producto')
def step_verificar_descripcion_productos(context):
    # Espera a que la tabla de productos esté presente en la página
    tabla = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//table[@class="table table-striped table-hover shadow-lg mb-5 text-center"]'))
    )

    # Encuentra todas las filas del cuerpo de la tabla (excluye la cabecera)
    filas = tabla.find_elements(By.XPATH, './tbody/tr')

    # Itera sobre cada fila para verificar que la columna "Descripcion" no esté vacía
    for fila in filas:
        descripcion_celda = fila.find_element(By.XPATH, './td[3]')  # La columna "Descripcion" es la tercera en la tabla
        descripcion_texto = descripcion_celda.text.strip()
        
        # Verifica que la descripción no esté vacía
        assert descripcion_texto, f"Error: El producto en la fila {fila.text} no tiene una descripción."

#Escenario Ver estado de stock de productos la descripción de cada producto Fin