+++
date = "2010-03-16"
title = "Como descativar sendmail en freebsd."
+++
Tengo una vps con la gente de [RootBSD.net](http://www.rootbsd.net/manage/aff.php?aff=027), y como en cualquier vps uno debe ahorrar todos los recursos que pueda, y como no necesito sendmail lo mejor sera desactivarlo. Para evitar que se ejecuta al iniciar el sistema edita el archivo /etc/rc.conf y agrega la siguiente linea.

> sendmail\_enable="no"y para detenerlo sin tener que reiniciar ejecuta el siguiente comando:> /etc/rc.d/sendmail stopListo :>.
