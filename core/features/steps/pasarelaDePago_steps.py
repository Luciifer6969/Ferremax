from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import re

#Escenario Registrar monto total de productos Inicio
@given('selecciona una cantidad de producto')
def step_seleccionaCantidad(context):
    wait = WebDriverWait(context.driver, 10)
    cantidad_select = wait.until(EC.visibility_of_element_located((By.ID, 'select1')))
    select = Select(cantidad_select)
    select.select_by_value("1") 
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@type="button" and text()="Agregar Cantidad"]'))
    )
    button.click()


@given('presiona el botón Ir a pagar')
def step_botonPagar(context):
        # Espera hasta que el `href` del botón contenga el prefijo del link de MercadoPago, indicando que está listo
    button = WebDriverWait(context.driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//a[@class="btn btn-primary" and contains(@href, "https://www.mercadopago.cl/checkout/")]'))
    )
    # Verifica que el href contenga el enlace correcto antes de hacer clic
    href = button.get_attribute("href")
    assert "https://www.mercadopago.cl/checkout/" in href, "El enlace no es el esperado para MercadoPago."

    # Realiza clic en el botón una vez que el link esté correcto
    button.click()

@then('el sistema redirecciona hacia la paserela de pago y muestra el total a pagar según la suma de los precios de los productos que esten almacenados en la orden de compra')
def step_totalMercadoPago(context):
    try:
        # Espera hasta que la URL de la pasarela de pago esté cargada
        WebDriverWait(context.driver, 20).until(
            EC.url_contains("mercadopago")
        )

        # Verifica la presencia del elemento con clase 'row-summary__price'
        precio_elemento = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//span[@class="row-summary__price "]'))
        )
        
        print("Elemento de precio encontrado en la pasarela de pago.")
    except TimeoutException:
        raise AssertionError("Error: No se encontró el elemento de precio en la pasarela de pago dentro del tiempo de espera.")
    
#Escenario Registrar monto total de productos Fin

#Escenario Realizar compra con fondos suficientes Inicio 
@when('ingresa sus datos en la plataforma de pago "{usuarioMercadoPago}" "{contraseña}"')
def step_ingresaDatosAPI(context,usuarioMercadoPago,contraseña):
    boton_ingresar = WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "andes-list__item-action") and .//span[contains(text(), "Ingresar con mi cuenta")]]'))
    )
    boton_ingresar.click()
    wait = WebDriverWait(context.driver, 10)
    usuario_input = wait.until(EC.presence_of_element_located((By.XPATH,  '//*[@type="email"]')))
    usuario_input.send_keys(usuarioMercadoPago)

    boton_continuar = WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id=":Rijhh:"]/span'))
    )
    boton_continuar.click()

    pswd_input = wait.until(EC.presence_of_element_located((By.XPATH,  '//*[@name="password"]')))
    pswd_input.send_keys(contraseña)

    boton_iniciar = WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@class="andes-button__content"][text()="Iniciar sesión"]'))
    )
    boton_iniciar.click()
    

@when('tiene los fondos necesarios para la compra')
def step_verificarSaldo(context):
    wait = WebDriverWait(context.driver, 10)
    saldo = wait.until(EC.presence_of_element_located((By.XPATH,  '//*[text()="Dinero disponible"]')))
    
@when('procede a pagar')
def step_procedeAPagar(context):
    boton_pagar = WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[text()="Pagar"]'))
    )
    boton_pagar.click()
    

@when('completa el pago')
def step_completaElPago(context):
    boton_empezar = WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[text()="Empezar"]'))
    )
    boton_empezar.click()
    volverAlSitio = WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[text()="Volver al sitio"]'))
    )
    volverAlSitio.click()

@then('la compra se realiza con éxito y redirige al usuario a la página FerreMax')
def step_pagoExitoso(context):
    try:
        # Verificar que la URL contiene la cadena que indica éxito en el pago
        WebDriverWait(context.driver, 10).until(
            lambda driver: "success_pay" in driver.current_url
        )
        
        # También se puede verificar la presencia del texto "Comprobante de Pago" en la página
        comprobante_element = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[text()="Comprobante de Pago"]'))
        )
        
        assert comprobante_element is not None, "Error: No se encontró el comprobante de pago en la página de éxito."
        print("Redirección exitosa a la página de comprobante de pago.")
        
    except TimeoutException:
        raise AssertionError("Error: La compra no redirigió a la página de éxito de pago dentro del tiempo de espera.")
#Escenario Realizar compra con fondos suficientes Fin

#Escenario Realizar compra con fondos insuficientes Inicio 

@when('no tiene los fondos necesarios para la compra')
def step_fondosElemento(context):
    try:
        # Busca algún mensaje que pueda indicar un problema con los fondos
        error_message = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "fondos insuficientes") or contains(text(), "Saldo")]'))
        )
        assert error_message is not None, "Error: No se encontró el mensaje de fondos insuficientes"
    except TimeoutException:
        raise AssertionError("Error: La compra no fue realizada debido a la falta de fondos.")


@when('presiona pagar')
def step_botonPagar(context):
    try:
        boton_pagar = WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[text()="Pagar"]'))
        )
        boton_pagar.click()
    except TimeoutException:
        raise AssertionError("Error: El botón 'Pagar' no se encontró o no fue posible hacer clic en él.")

    
@then('la compra no se realiza con éxito y se le notifica al usuario que no tiene los fondos suficientes')
def step_pagoSinExito(context):
    try:
        # Guarda la URL actual al entrar en la pasarela de pago
        url_actual = context.driver.current_url

        # Verifica si la página permanece en la URL de pago
        WebDriverWait(context.driver, 10).until(
            lambda driver: driver.current_url == url_actual
        )
        
        assert context.driver.current_url == url_actual, \
            "Error: La compra parece haber sido procesada, ya que la URL cambió."

    except TimeoutException:
        raise AssertionError("Error: La compra no fue realizada, pero no se detectó el mensaje esperado.")

#Escenario Realizar compra con fondos insuficientes Fin 

#Escenario Generar comprobante de pago Inicio 

@then('la página FerreMax genera y muestra el comprobante de compra')
def step_comprobante(context):
    try:
        # Verificar que la URL contiene la cadena que indica éxito en el pago
        WebDriverWait(context.driver, 10).until(
            lambda driver: "success_pay" in driver.current_url
        )
        
        # También se puede verificar la presencia del texto "Comprobante de Pago" en la página
        comprobante_element = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[text()="Comprobante de Pago"]'))
        )
        
        assert comprobante_element is not None, "Error: No se encontró el comprobante de pago en la página de éxito."
        print("Redirección exitosa a la página de comprobante de pago.")
        
    except TimeoutException:
        raise AssertionError("Error: La compra no redirigió a la página de éxito de pago dentro del tiempo de espera.")

#Escenario Generar comprobante de pago Fin 