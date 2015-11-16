+++
date = "2010-04-28"
title = "Freebsd /usr/ports: No such file or directory."
+++
He instalado freebsd en una maquina virtual para luego ver si me decido hacerlo mi sistema de escritorio, y me he encontrado con el problema de que el directorio /usr/ports no existe. Para solucionar este problema se puede hacer lo siguiente:

> csup -h cvsup.us.freebsd.org /usr/share/examples/cvsup/ports-supfile
