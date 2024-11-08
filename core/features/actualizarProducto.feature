Feature: Actualización de productos en FerreMax
 ñ
  Scenario: Actualizar nombre de un producto
    Given que un usuario ingresó a la página "FerreMax"
    When se dirige a iniciar sesión
    And el usuario está registrado como bodeguero "bodeguero@gmail.com" "contrasena1"
    And el usuario tiene una sesión iniciada
    And presiona el botón 'Actualizar producto'
    And selecciona un producto para actualizar
    And presiona el botón "actualizar"
    And cambia el nombre del producto a través del formulario
    And cambia el nombre del producto "cambio de nombre"
    And presiona el botón 'Actualizar producto'
    Then el sistema actualiza el producto y notifica al usuario que el producto se actualizó con éxito

  Scenario: Actualizar stock de un producto
    Given que un usuario ingresó a la página "FerreMax"
    When se dirige a iniciar sesión
    And el usuario está registrado como bodeguero "bodeguero@gmail.com" "contrasena1"
    And el usuario tiene una sesión iniciada
    And presiona el botón 'Actualizar producto'
    And selecciona un producto para actualizar
    And presiona el botón "actualizar"
    And cambia el stock del producto a través del formulario
    And cambia el stock del producto "20"
    And presiona el botón 'Actualizar producto'

    Then el sistema actualiza el producto y notifica al usuario que el producto se actualizó con éxito

  Scenario: Actualizar descripción de un producto
    Given que un usuario ingresó a la página "FerreMax"
    When se dirige a iniciar sesión
    And el usuario está registrado como bodeguero "bodeguero@gmail.com" "contrasena1"
    And el usuario tiene una sesión iniciada
    And presiona el botón 'Actualizar producto'
    And selecciona un producto para actualizar
    And presiona el botón "actualizar"
    And cambia la descripción del producto a través del formulario
    And cambia la descripción del producto "descripción de prueba"
    And presiona el botón 'Actualizar producto'
    Then el sistema actualiza el producto y notifica al usuario que el producto se actualizó con éxito

  Scenario: Actualizar precio de un producto
    Given que un usuario ingresó a la página "FerreMax"
    When se dirige a iniciar sesión
    And el usuario está registrado como bodeguero "bodeguero@gmail.com" "contrasena1"
    And tiene una sesión iniciada
    And presiona el botón 'Actualizar producto'
    And selecciona un producto para actualizar
    And presiona el botón "actualizar"
    And cambia el precio del producto a través del formulario
    And cambia el precio del producto "30000"
    And presiona el botón 'Actualizar producto'
    Then el sistema actualiza el producto y notifica al usuario que el producto se actualizó con éxito
