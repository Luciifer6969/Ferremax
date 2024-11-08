Feature: Agregar producto

    Scenario: Agregar producto exitoso
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When accede al menú Agregar Producto
    And completa la casilla Nombre Producto "prueba producto"
    And completa la casilla Marca "Total"
    And completa la casilla Precio "10000"
    And completa la casilla Categoría "Herramientas manuales"
    And completa la casilla Imagen "https://media.tenor.com/yNMGjXsoYGUAAAAe/cat-cats.png"
    And completa la casilla Descripción "descripcion de prueba"
    And completa la casilla Cantidad "5"
    And presiona el botón Agregar producto
    Then el producto se agrega al inventario de la página y notifica al usuario que el producto fue agregado correctamente


    Scenario: Agregar producto erróneo sin el nombre de producto
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When accede al menú Agregar Producto
    And no completa la casilla Nombre Producto
    And completa la casilla Marca "Total"
    And completa la casilla Precio "10000"
    And completa la casilla Categoría "Herramientas manuales"
    And completa la casilla Imagen "https://media.tenor.com/yNMGjXsoYGUAAAAe/cat-cats.png"
    And completa la casilla Descripción "descripcion de prueba"
    And no completa la casilla Cantidad 
    And presiona el botón Agregar producto
    Then el producto no es agregado al inventario y notifica al usuario que falta completar el campo Nombre Producto

    Scenario: Agregar producto erróneo sin la descripción del producto 
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When accede al menú Agregar Producto
    And completa la casilla Nombre Producto "prueba producto"
    And completa la casilla Marca "Total"
    And completa la casilla Precio "10000"
    And completa la casilla Categoría "Herramientas manuales"
    And completa la casilla Imagen "https://media.tenor.com/yNMGjXsoYGUAAAAe/cat-cats.png"
    And no completa la casilla Descripción 
    And completa la casilla Cantidad "5"
    And presiona el botón Agregar producto
    Then el producto no es agregado al inventario y notifica al usuario que falta completar el campo Descripción

    Scenario: Agregar producto exitoso sin imagen
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When accede al menú Agregar Producto
    And completa la casilla Nombre Producto "prueba producto"
    And completa la casilla Marca "Total"
    And completa la casilla Precio "10000"
    And completa la casilla Categoría "Herramientas manuales"
    And no completa la casilla Imagen 
    And completa la casilla Descripción "descripcion de prueba"
    And completa la casilla Cantidad "5"
    And presiona el botón Agregar producto
    Then el producto no es agregado al inventario y notifica al usuario que falta completar el campo Imagen de producto

    Scenario: Agregar producto erróneo sin cantidad del producto
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When accede al menú Agregar Producto
    And completa la casilla Nombre Producto "prueba producto"
    And completa la casilla Marca "Total"
    And completa la casilla Precio "10000"
    And completa la casilla Categoría "Herramientas manuales"
    And completa la casilla Imagen "https://media.tenor.com/yNMGjXsoYGUAAAAe/cat-cats.png" 
    And completa la casilla Descripción "descripcion de prueba"
    And no completa la casilla Cantidad
    And presiona el botón Agregar producto
    Then el producto no es agregado al inventario y notifica al usuario que falta completar el campo Cantidad de producto

    Scenario: Agregar producto erróneo sin precio del producto
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When accede al menú Agregar Producto
    And completa la casilla Nombre Producto "prueba producto"
    And completa la casilla Marca "Total"
    And no completa la casilla Precio
    And completa la casilla Categoría "Herramientas manuales"
    And completa la casilla Imagen "https://media.tenor.com/yNMGjXsoYGUAAAAe/cat-cats.png" 
    And completa la casilla Descripción "descripcion de prueba"
    And completa la casilla Cantidad "5"
    And presiona el botón Agregar producto
    Then el producto no es agregado al inventario y notifica al usuario que falta completar el campo Precio del producto

    Scenario: Agregar producto erróneo sin categoría 
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When accede al menú Agregar Producto
    And completa la casilla Nombre Producto "prueba producto"
    And completa la casilla Marca "Total"
    And completa la casilla Precio "10000"
    And no completa la casilla categoría
    And completa la casilla Imagen "https://media.tenor.com/yNMGjXsoYGUAAAAe/cat-cats.png" 
    And completa la casilla Descripción "descripcion de prueba"
    And completa la casilla Cantidad "5"
    And presiona el botón Agregar producto
    Then el producto no es agregado al inventario y notifica al usuario que falta completar el campo categoría del producto

    Scenario: Agregar producto erróneo sin marca
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When accede al menú Agregar Producto
    And completa la casilla Nombre Producto "prueba producto"
    And no completa la casilla Marca
    And completa la casilla Precio "10000"
    And completa la casilla Categoría "Herramientas manuales"
    And completa la casilla Imagen "https://media.tenor.com/yNMGjXsoYGUAAAAe/cat-cats.png" 
    And completa la casilla Descripción "descripcion de prueba"
    And completa la casilla Cantidad "5"
    And presiona el botón Agregar producto
    Then el producto no es agregado al inventario y notifica al usuario que falta completar el campo Marca del producto

    Scenario: Redirección del botón Cancelar 
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When accede al menú Agregar Producto
    And presiona el botón Cancelar
    Then el usuario es redirigido a la página principal de FerreMax

    Scenario: Ingreso de caracteres especiales en formulario agregar producto
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When accede al menú Agregar Producto
    And completa la casilla Nombre Producto "!%!'$##'"
    And completa la casilla Marca "Total"
    And completa la casilla Precio "1"
    And completa la casilla Categoría "Herramientas manuales"
    And completa la casilla Imagen "!%!'$##'"
    And completa la casilla Descripción "!%!'$##'"
    And completa la casilla Cantidad "1"
    And presiona el botón Agregar producto
    Then el sistema no agrega el producto y notifica al usuario que no se acepta caracteres especiales

    Scenario: Ingresar un producto con valor negativo en precio de producto
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When accede al menú Agregar Producto
    And completa la casilla Nombre Producto "prueba producto"
    And completa la casilla Marca "Total"
    And completa la casilla Precio "-100"
    And completa la casilla Categoría "Herramientas manuales"
    And completa la casilla Imagen "https://media.tenor.com/yNMGjXsoYGUAAAAe/cat-cats.png" 
    And completa la casilla Descripción "descripcion de prueba"
    And completa la casilla Cantidad "5"
    And presiona el botón Agregar producto
    Then el producto no es agregado al inventario y notifica al usuario que el precio debe ser mayor a 0 

    Scenario: Ingresar un producto con valor negativo en cantidad de producto
    Given que un usuario bodeguero ingresó a la página FerreMax "bodeguero@gmail.com" "contrasena1"
    When accede al menú Agregar Producto
    And completa la casilla Nombre Producto "prueba producto"
    And completa la casilla Marca "Total"
    And completa la casilla Precio "10000"
    And completa la casilla Categoría "Herramientas manuales"
    And completa la casilla Imagen "https://media.tenor.com/yNMGjXsoYGUAAAAe/cat-cats.png" 
    And completa la casilla Descripción "descripcion de prueba"
    And completa la casilla Cantidad "-10"
    And presiona el botón Agregar producto
    Then el producto no es agregado al inventario y notifica al usuario que la cantidad debe ser mayor a 0 