+++
date = "2007-12-03"
title = "Samba + Vista"
+++
Mini Manual de como usar samba en una red de equipos con windows vista. Primero vamos a listar los recursos compartidos, que se hace de la siguiente manera:

> smbcliente -L jesus-pc -U jesusdonde jesus-pc es el nombre del equipo y jesus el nombre de usuario. y nos mostrara una salida como esta:> [root@localhost ~]# smbclient -L jesus-pc -U jesus Password: Domain=[JESUS-PC] OS=[Windows Vista (TM) Ultimate 6000] Server=[Windows Vista (TM) Ultimate 6.0] Sharename Type Comment --------- ---- ------- ADMIN$ Disk Remote Admin C Disk C$ Disk Default share compartido Disk IPC$ IPC Remote IPC Domain=[JESUS-PC] OS=[Windows Vista (TM) Ultimate 6000] Server=[Windows Vista (TM) Ultimate 6.0] Server Comment --------- ------- Workgroup Master --------- -------Vemos que esta compartido un directorio llamado compartir y la unidad C, para acceder a ellos es bastante facil. simplemente escribe en la consola lo siguiente:> smbclient //jesus-pc/compartido -U jesuste pedir password de nuevo y ya que entre podras ejecutar comandos como si de ftp se tratara, teclea help para ver los comandos disponibles y eso es todo :p
