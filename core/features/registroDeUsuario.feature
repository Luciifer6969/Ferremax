Feature: Registro de usuario 

    Scenario: Registro de usuario exitoso
    Given  que un usuario ingresó a la página FerreMax
    When accede a la opción de Registrarse
    And completa el campo Nombre Usuario
    And completa el campo Nombre
    And completa el campo Apellido
    And completa el campo Correo electrónico
    And completa el campo Confirme correo electrónico
    And completa el campo Contraseña
    And completa el campo Confirme contraseña
    And presiona el boton Registrarse
    Then  el sistema registra el usuario y se redige al menú principal 