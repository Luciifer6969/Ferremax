Feature: Carrito de compra

    Background:
    Given que un usuario ingresó a la página FerreMax
    When accede a la opción de ingresar
    And ingresa una dirección de "cliente@gmail.com" registrado previamente
    And ingresa la contraseña correcta "contrasena1"
    And presiona el botón ingresar
    And tiene una sesión iniciada

    Scenario: Agregar producto
    Given tiene una sesión iniciada
    And ingresa al menú de productos
    When elige un producto del menú
    And presiona el botón Agregar al carrito en el producto deseado 
    Then el producto es agregado al carrito de compras de la página
    
    Scenario: Modificar cantidad del producto en el carrito de compra
    Given tiene productos agregados al carrito
    And ingresa al menú Carrito de compra
    When selecciona una cantidad de producto
    And selecciona el botón Agregar cantidad
    Then se modifica la cantidad de producto

    Scenario: Eliminar producto del carrito de compra
    Given tiene productos agregados al carrito 
    And ingresa al menú Carrito de compra
    And presiona el botón Eliminar producto
    Then el producto es eliminado del carrito  

    Scenario: Calcular el total de productos
    Given tiene productos agregados al carrito 
    And ingresa al menú Carrito de compra
    And tiene selecionada una cantidad de productos
    Then el sistema calcula el valor total del carrito y muestra ese dato

    