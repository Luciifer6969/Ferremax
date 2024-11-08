Feature: Pasarela de pago 

    Background: 
    Given que un usuario ingresó a la página FerreMax
    When accede a la opción de ingresar
    And ingresa una dirección de "cliente@gmail.com" registrado previamente
    And ingresa la contraseña correcta "contrasena1"
    And presiona el botón ingresar
    And tiene una sesión iniciada

    Scenario: Registrar monto total de productos  
    Given tiene productos agregados al carrito 
    And ingresa al menú Carrito de compra 
    And selecciona una cantidad de producto
    And presiona el botón Ir a pagar
    Then el sistema redirecciona hacia la paserela de pago y muestra el total a pagar según la suma de los precios de los productos que esten almacenados en la orden de compra

    Scenario: Realizar compra con fondos suficientes
    Given tiene productos agregados al carrito 
    And ingresa al menú Carrito de compra 
    And selecciona una cantidad de producto
    And presiona el botón Ir a pagar
    When ingresa sus datos en la plataforma de pago "TESTUSER1596276845" "Hg1yAWPqXw"
    And tiene los fondos necesarios para la compra
    And procede a pagar  
    And completa el pago
    Then la compra se realiza con éxito y redirige al usuario a la página FerreMax

    Scenario: Realizar compra con fondos insuficientes
    Given tiene productos agregados al carrito 
    And ingresa al menú Carrito de compra 
    And selecciona una cantidad de producto
    And presiona el botón Ir a pagar
    When ingresa sus datos en la plataforma de pago "TESTUSER1312952289" "5MEDlWj3Vd"
    And no tiene los fondos necesarios para la compra
    And presiona pagar
    Then la compra no se realiza con éxito y se le notifica al usuario que no tiene los fondos suficientes

    Scenario: Generar comprobante de pago
    Given tiene productos agregados al carrito 
    And ingresa al menú Carrito de compra
    And selecciona una cantidad de producto
    And presiona el botón Ir a pagar
    When ingresa sus datos en la plataforma de pago "TESTUSER1596276845" "Hg1yAWPqXw"
    And tiene los fondos necesarios para la compra
    And procede a pagar  
    And completa el pago
    Then la página FerreMax genera y muestra el comprobante de compra