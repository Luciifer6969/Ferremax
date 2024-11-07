Feature: Carrito de compra

    Background:
    Given que un usuario ingresó a la página FerreMax
    When accede a la opción de ingresar
    And ingresa una dirección de "cliente@gmail.com" registrado previamente
    And ingresa la contraseña correcta "contrasena1"
    And presiona el botón ingresar
    And tiene una sesión iniciada

    Scenario: Agregar producto
    And tiene una sesión iniciada
    And ingresa al menú de productos
    And elige un producto del menú
    And presiona el botón Agregar al carrito en el producto deseado 
    Then el producto es agregado al carrito de compras de la página