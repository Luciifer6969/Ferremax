Feature: Inicio sesión 

  Scenario: Inicio sesión con usuario correcto con contraseña válida
  Given  que un usuario ingresó a la página FerreMax
  When  accede a la opción de ingresar
  And ingresa una dirección de "cliente@gmail.com" registrado previamente
  And ingresa la contraseña correcta "contrasena1"
  And presiona el botón ingresar
  Then el usuario inicia sesión correctamente 
  

  Scenario: Inicio sesión con usuario incorrecto
  Given  que un usuario ingresó a la página FerreMax
  When accede a la opción de ingresar
  And ingresa una dirección de "clientes1@gmail.com" correo no registrado
  And   ingresa la contraseña correcta "contrasena1"
  And   presiona el botón ingresar
  Then  el usuario no puede iniciar sesión 

  Scenario: Inicio sesión con usuario correcto y con contraseña inválida
  Given  que un usuario ingresó a la página FerreMax
  When  accede a la opción de ingresar
  And   ingresa una dirección de "cliente@gmail.com" registrado previamente
  And   ingresa una contraseña incorrecta "contrasena"
  And   presiona el botón ingresar
  Then  el usuario no puede iniciar sesión y ve una alerta de contraseña incorrecta

  Scenario: El usuario ingresa un correo válido y en el campo de contraseña ingresa una injección sql
  Given que un usuario ingresó a la página FerreMax
  When accede a la opción de ingresar
  And ingresa una dirección de "cliente@gmail.com" registrado previamente
  And ingresa una contraseña incorrecta "asdf’ OR ‘a’=’a " 
  Then el usuario no puede iniciar sesión y se ve una alerta de tipo de datos en el campo contraseña no son válidos

  Scenario: Redirección del botón 'Cancelar'
  Given que un usuario ingresó a la página FerreMax
  When accede a la opción de ingresar
  And presiona el botón cancelar
  Then el usuario no puede iniciar sesión y se redirige al Home

  Scenario: Ingreso de email con formato incorrecto 
  Given que un usuario ingresó a la página FerreMax
  When accede a la opción de ingresar
  And completa el campo de correo con un mail registrado sin agregar @ "clientegmail.com"
  And ingresa la contraseña correcta "contrasena1"
  Then el usuario no puede iniciar sesión y se ve una alerta notificando formato de correo no válido, incluye un @ en la dirección de correo electrónico

  Scenario:
  