+++
date = "2010-03-09"
title = "VLC como root."
+++
Vlc no se puede ejecutar como root en debian, gentoo y probablemente otras distribuciones. Aqui esta la solucion en el caso de debian. 1.- Obtener el codigo fuente.

> apt-get source vlc2.- Instalar dependencias para compilar> apt-get build-dep vlc3.- Configurar> ./configure --enable-run-as-root4.- Compilar e instalar> ./compile && make install
