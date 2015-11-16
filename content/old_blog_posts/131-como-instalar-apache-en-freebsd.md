+++
date = "2010-03-13"
title = "Como instalar apache en freebsd"
+++
Nos vamos al directorio del port en este caso yo quiero apache 2.2

> cd /usr/ports/www/apache22/y ejecutamos:> make install cleanAgregamos la siguiente linea a /etc/rc.conf para que apache inicie al iniciar el sistema.> apache22\_enable="YES"Para iniciar de forma manual apache podemos usar el siguiente comando:> apachectl startAcepta las opciones restart, graceful y stop, restart y stop se describen por si mismas, graceful es un restart sin forzar. Tambien podemos usar la opcion configtest que nos dice si los archivos de configuracion no tienen errores. Ejemplo:> [root@host ~]# /usr/local/sbin/apachectl configtest Syntax OK
