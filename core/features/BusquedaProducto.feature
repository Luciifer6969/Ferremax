Feature: Búsqueda de productos en FerreMax

  Scenario: Búsqueda de productos por nombre del producto
    Given que un usuario ha accedido a la página principal de "FerreMax"
    When accede a la página principal
    And se dirige al campo de buscar
    And ingresa el nombre de un producto "taladro"
    And presiona el botón buscar
    Then el sistema realiza la búsqueda del producto y lo muestra en caso de ser encontrado

  Scenario: Búsqueda de productos por el nombre de la categoría del producto
    Given que un usuario ha accedido a la página principal de "FerreMax"
    When accede a la página principal
    And se dirige al campo de buscar
    And ingresa una categoría de producto "herramientas manuales"
    And presiona el botón buscar
    Then el sistema realiza la búsqueda de los productos que sean de esa categoría y los muestra en caso de ser encontrados

  Scenario: Búsqueda de productos por marca de producto
    Given que un usuario ha accedido a la página principal de "FerreMax"
    When accede a la página principal
    And se dirige al campo de buscar
    And ingresa una marca de producto "herramientas Manuales"
    And presiona el botón buscar
    Then el sistema realiza la búsqueda de los productos que sean de esa marca y los muestra en caso de ser encontrados

  Scenario: Búsqueda de productos errónea
    Given que un usuario ha accedido a la página principal de "FerreMax"
    When accede a la página principal
    And se dirige al campo de buscar 
    And ingresa un producto que no existe '"veloti"
    Then el sistema muestra un mensaje por antalla indicando que no se encontraron resultados relacionados y muestra un enlace para ver los productos disponibles
