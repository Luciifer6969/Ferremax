Feature: Eliminar producto

    Scenario: Eliminar producto exitoso
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When ingresa al menú Eliminar Producto
    And selecciona un producto a eliminar 
    And presiona el botón eliminar
    Then la página se actualiza eliminando el producto y notificando al usuario El producto fue eliminado con éxito

    Scenario: Eliminar categoría de producto exitosa
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When ingresa al menú Eliminar Producto
    And selecciona una categoría "Herramientas Manuales"
    And presiona el botón Eliminar categoría
    Then la página se actualiza eliminando la categoría seleccionada y notificando al usuario La categoría se ha eliminado con éxito

    Scenario: Eliminar múltiples productos
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When ingresa al menú Eliminar Producto
    And selecciona un producto a eliminar 
    And selecciona otro producto
    And presiona el botón Eliminar seleccionados
    Then la página se actualiza eliminando el producto y notificando al usuario El producto fue eliminado con éxito

    Scenario:Presionar eliminar sin seleccionar producto
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When ingresa al menú Eliminar Producto
    And no selecciona ningún producto a eliminar 
    And  presiona el botón Eliminar seleccionado
    Then el sistema muestra un mensaje señalando que No se Seleccionó ningún producto para eliminar.