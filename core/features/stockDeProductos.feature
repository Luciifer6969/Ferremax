Feature: Stock de productos

    Scenario: Ver estado de stock de productos desde usuario Vendedor
    Given que un usuario ingresó a la página Ferremax
    And el usuario está registrado como vendedor "vendedor@gmail.com" "contrasena1"
    And tiene una sesión iniciada 
    When selecciona el menú stock disponible
    Then el sistema muestra información sobre productos, nombres, precio, cantidad disponible

    Scenario: Ver estado de stock de productos desde usuario no registrado
    Given que un usuario ingresó a la página Ferremax
    And el usuario no está registrado
    And no tiene una sesión iniciada
    Then el sistema no habilita el menú de stock de productos

    Scenario: Ver estado de stock de productos desde usuario Bodeguero
    Given que un usuario ingresó a la página Ferremax
    And el usuario está registrado como bodeguero "bodeguero@gmail.com" "contrasena1"
    And  tiene una sesión iniciada 
    Then el sistema no habilita el menú de stock de productos por falta de permisos

    Scenario: Ver estado de stock de productos la descripción de cada producto
    Given que un usuario ingresó a la página Ferremax
    And el usuario está registrado como vendedor "vendedor@gmail.com" "contrasena1"
    And tiene una sesión iniciada
    When selecciona el menú Stock disponible
    Then el sistema muestra información sobre la descripción del producto