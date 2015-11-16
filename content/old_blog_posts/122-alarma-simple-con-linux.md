+++
date = "2010-02-08"
title = "Alarma simple con linux."
+++
Crear alarmas en linux es bastante facil. **1.- Instalar Software.** Ubuntu/Debian

> sudo aptitude install libnotify **2.- Creando la alarma propiamente dicho.**** Ejemplo: Agua para el cafe. **> sleep 10m && notify-send "El agua del cafe esta lista." &simplemente escribe esa linea en alguna consola/terminal, o presiona Alt-F2 en el caso de Ubuntu y escribe ese comando, presiona enter, al parecer nada cambio, pero si esperas 5 minutos se mostrara un mensaje en tu pantalla con el texto el agua esta lista.** Explicacin:**El comando sleep acepta como parametros s,h,d,m, para segundos, horas, dias, meses, por ejemplo para 1 segundo seria sleep 1s, lo que hace el comando sleep es solamente no hacer nada por el tiempo que se le especifique. Luego tenemos los simbolos && que significan que se espere a que termine el comando anterior en este caso sleep 10m a que finalice. El comando notify-send es el que nos muestra el mensaje en la pantalla, por ejemplo notify-send "hola", mostrara un hola en tu pantalla checa el screen shot.<center>
<a href="http://Pictat.com/show.php?i=/2010/2/7/257652010020713.png" target="_blank"><img src="http://Pictat.com/t/2010/2/7/257652010020713.png" border="0" alt="Free Image Hosting at www.Pictat.com"></a> </center>Todos los comandos se pueden usar por separado o combinarlos.
