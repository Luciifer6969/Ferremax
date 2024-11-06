Feature: Consulta producto

    Background:
    Given que un usuario ingresó a la página FerreMax
    When accede a la opción de ingresar
    And ingresa una dirección de "cliente@gmail.com" registrado previamente
    And ingresa la contraseña correcta "contrasena1"
    And presiona el botón ingresar
    And tiene una sesión iniciada

    Scenario: Consulta de producto exitosa
    When ingresa al menú de consulta
    And ingresa a la opción Consultar producto
    And ingresa un motivo de consulta "prueba motivo"
    And selecciona un producto del inventario "Taladro de impacto 13 mm 680W TG1061356 Total"
    And completa la casilla de comentarios "prueba de comentario"
    And presiona el botón Enviar comentario
    Then se envía la consulta con éxito

    Scenario: Consulta de producto erróneo sin selección de producto
    And ingresa al menú de consulta
    And ingresa a la opción Consultar producto 
    And ingresa un motivo de consulta "prueba motivo"
    And no selecciona un producto del inventario 
    And completa la casilla de comentarios "prueba de comentario"
    And presiona el botón Enviar comentario
    Then no se envía la consulta con éxito y se notifica al usuario que no se puede realizar la consulta