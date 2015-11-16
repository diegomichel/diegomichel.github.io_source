+++
date = "2009-08-16"
title = "Proteger paginas con .htaccess"
+++
Esta es una forma rapida de proteger tus paginas de los mirones. **Paso 1** Crear el archivo de contrasenas, reemplaza USUARIO por tu nombre de usuario.

> htpasswd -c .htpassword USUARIOSe te preguntara el password para tu usuario, los escribes y listo. **Paso 2** Crear el archivo .htaccess, abre el archivo .htaccess en el directorio que quieras proteger y escribe las siguientes lineas:> AuthUserFile /var/www/directorioprotegido/.htpassword AuthName Bienvenido AuthType Basic Require valid-user **AuthUserFile** Es donde se encuentra tu archivo .htpassword **AuthName** Mensaje que se mostrara en la ventana de entrada **AuthType** Tipo de autentificacion. **Require valid-user** Se requiere un usuario y contrasena valido para poder entrar. Listo ya tienes tu directorio protegido con contrasena via htaccess y htpasswd
