+++
date = "2010-03-13"
title = "Como instalar bash en freebsd"
+++
Entra a tu maquina como root y ejecuta los siguientes comandos.

> portsnap update extract cd /usr/ports/shells/bash make install cleanAhora ponemos bash como default> chsh -s /usr/local/bin/bash diegoy listo la proxima vez que hagas login tendras a bash como default.
