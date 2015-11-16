+++
date = "2008-12-29"
title = "Prevenir timeout en conecciones ssh"
+++
Simplemente en la maquina cliente se edita el archivo /etc/ssh/ssh\_config y se anade al final la siguiente linea:

> ServerAliveInterval 5Lo que hace es enviar una senal cada 5 segundos para que no se cierre la sesin.
