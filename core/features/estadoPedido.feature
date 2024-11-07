Feature: Estado de pedidos

    Scenario: Aprobar el estado del pedido desde usuario Vendedor 
    Given que un usuario ingresó a la página Ferremax 
    And el usuario está registrado como vendedor "vendedor@gmail.com" "contrasena1"
    And tiene una sesión iniciada
    When  ingresa al menú de estado de pedidos
    And selecciona el botón aprobar
    Then el sistema muestra un mensaje en pantalla indicando que el estado del pedido fue aprobado correctamente

    Scenario: Modificar estado del pedido desde usuario no registrado
    Given que un usuario ingresó a la página Ferremax
    And el usuario no está registrado
    When intenta acceder al menú de estado de pedidos
    Then el sistema no habilita el acceso al menú de estado de pedidos

    Scenario: Modificar estado del pedido desde usuario cliente registrado
    Given que un usuario ingresó a la página Ferremax
    And el usuario está registrado como cliente "cliente@gmail.com" "contrasena1"
    And tiene una sesión iniciada
    When intenta acceder al menú de estado de pedidos
    Then el sistema no habilita el acceso al menú de estado de pedidos por falta de permisos

    Scenario: Modificar estado del pedido desde usuario Bodeguero
    Given que un usuario ingresó a la página Ferremax
    And  el usuario está registrado como bodeguero "bodeguero@gmail.com" "contrasena1"
    And  tiene una sesión iniciada
    When intenta acceder al menú de estado de pedidos
    Then el sistema no habilita el acceso al menú de estado de pedidos por falta de permisos