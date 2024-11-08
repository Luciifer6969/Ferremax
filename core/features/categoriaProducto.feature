Feature: Categoria de productos

    Scenario:Seleccionar productos por categorías
    Given que un usuario ingresó a la página "FerreMax"
    When accede a la página principal
    And se dirige a la página de catálogo de productos
    And filtra por categoría
    And presiona la categoría a filtrar
    Then el sistema realiza la búsqueda del producto y lo muestra en caso de ser encontrado
    
    Scenario:Seleccionar categorías sin productos asociados
    Given que un usuario ingresó a la página "FerreMax"
    When accede a la página principal
    And se dirige a la página de catálogo de productos
    And filtra por categoría
    And presiona el boton filtrar 
    Then el sistema muestra un mensaje diciendo "Lo sentimos, no contamos con productos registrados"
    
    Scenario:Navegación de productos a través de páginas
    Given que un usuario ingresó a la página "FerreMax"
    When accede a la página productos
    And se dirige al final de los productos
    And selecciona la página 2 
    Then el sistema redirecciona a la segunda página visualizando el resto de productos
    
    Scenario:Navegación de productos filtrado por categorías a través de páginas
    Given que un usuario ingresó a la página "FerreMax"
    When accede a la página productos
    And selecciona una categoría de producto
    And se dirige al final de los productos
    And selecciona la página 2 
    Then el sistema redirecciona a la segunda página visualizando el resto de productos filtrados por la categoría 