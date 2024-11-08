from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL de la página
URL = "http://127.0.0.1:8000"  # Asegúrate de que esta URL sea correcta

# Elementos de la página
SEARCH_INPUT_XPATH = '//*[@id="navbarSupportedContent"]/form/input'
SEARCH_BUTTON_XPATH = '//*[@id="navbarSupportedContent"]/form/button'

# Background steps

@given('que un usuario ingresó a la página "FerreMax"')
def step_open_homepage(context):
    context.driver.get("http://127.0.0.1:8000/")

@given('que un usuario ha accedido a la página principal de "FerreMax"')
def step_usuario_accede_pagina(context):
    context.driver.get("http://127.0.0.1:8000")

@when('se dirige al campo de buscar')
def step_dirige_campo_buscar(context):
    context.search_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, SEARCH_INPUT_XPATH))
    )

@when('ingresa el nombre de un producto "{producto}"')
def step_ingresa_nombre_producto(context, producto):
    context.search_input.clear()
    context.search_input.send_keys(producto)

@when('ingresa una categoría de producto "{categoria}"')
def step_ingresa_categoria_producto(context, categoria):
    context.search_input.clear()
    context.search_input.send_keys(categoria)

@when('ingresa una marca de producto "{marca}"')
def step_ingresa_marca_producto(context, marca):
    context.search_input.clear()
    context.search_input.send_keys(marca)

@when('ingresa un producto que no existe "{producto_no_existente}"')
def step_ingresa_producto_no_existente(context, producto_no_existente):
    context.search_input.clear()
    context.search_input.send_keys(producto_no_existente)

@when('presiona el botón buscar')
def step_presiona_boton_buscar(context):
    search_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, SEARCH_BUTTON_XPATH))
    )
    search_button.click()

@then('el sistema realiza la búsqueda del producto y lo muestra en caso de ser encontrado')
def step_verifica_producto_encontrado(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "producto-encontrado")]'))
    )

@then('el sistema realiza la búsqueda de los productos que sean de esa categoría y los muestra en caso de ser encontrados')
def step_verifica_categoria_encontrada(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "producto-categoria-encontrada")]'))
    )

@then('el sistema realiza la búsqueda de los productos que sean de esa marca y los muestra en caso de ser encontrados')
def step_verifica_marca_encontrada(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "producto-marca-encontrada")]'))
    )

@then('el sistema muestra un mensaje por pantalla indicando que no se encontraron resultados relacionados y muestra un enlace para ver los productos disponibles')
def step_verifica_mensaje_error(context):
    error_message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "alert alert-warning")]'))
    )
    assert "no se encontraron resultados relacionados" in error_message.text.lower(), \
        "El mensaje de error esperado no se mostró."
