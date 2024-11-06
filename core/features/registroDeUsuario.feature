Feature: Registro de usuario 

    Scenario: Registro de usuario exitoso
    Given  que un usuario ingresó a la página FerreMax
    When accede a la opción de Registrarse
    And completa el campo Nombre Usuario "cliente"
    And completa el campo Nombre "cliente"
    And completa el campo Apellido "cliente"
    And completa el campo Correo electrónico "cliente@gmail.com"
    And completa el campo Confirme correo electrónico "cliente@gmail.com"
    And completa el campo Contraseña "contrasena1"
    And completa el campo Confirme contraseña "contrasena1"
    And presiona el boton Registrarse
    Then  el sistema registra el usuario y se redige al menú principal 

    Scenario: Registro de usuario erróneo sin nombre de usuario
    Given que un usuario ingresó a la página FerreMax
    When accede a la opción de Registrarse  
    And deja vacío el campo Nombre Usuario 
    And completa el campo Nombre "prueba" 
    And completa el campo Apellido "prueba" 
    And completa el campo Correo electrónico "prueba@gmail.com"
    And completa el campo Confirme correo electrónico "prueba@gmail.com"
    And completa el campo Contraseña "contrasena1"
    And completa el campo Confirme contraseña "contrasena1"
    And presiona el boton Registrarse
    Then el sistema no permite el registro y notifica que hay un campo incompleto en el formulario

    Scenario: Registro de usuario erróneo sin nombre
    Given que un usuario ingresó a la página FerreMax
    When accede a la opción de Registrarse  
    And completa el campo Nombre Usuario "prueba" 
    And deja vacío el campo Nombre 
    And completa el campo Apellido "prueba" 
    And completa el campo Correo electrónico "prueba@gmail.com"
    And completa el campo Confirme correo electrónico "prueba@gmail.com"
    And completa el campo Contraseña "contrasena1"
    And completa el campo Confirme contraseña "contrasena1"
    And presiona el boton Registrarse
    Then el sistema no permite el registro y notifica que hay un campo incompleto en el formulario

    Scenario: Registro de usuario erróneo con correos electronicos diferentes
    Given  que un usuario ingresó a la página FerreMax
    When accede a la opción de Registrarse
    And completa el campo Nombre Usuario "prueba" 
    And completa el campo Nombre "prueba" 
    And completa el campo Apellido "prueba" 
    And completa el campo Correo electrónico "prueba@gmail.com"
    And completa el campo Confirme correo electrónico con un correo diferente "otraprueba@gmail.com"
    And completa el campo Contraseña "contrasena1"
    And completa el campo Confirme contraseña "contrasena1"
    And presiona el boton Registrarse
    Then el sistema no permite el registro y notifica que los campos Correo electrónico y Confirme correo electrónico no coinciden