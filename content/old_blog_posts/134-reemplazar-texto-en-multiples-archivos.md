+++
date = "2010-03-18"
title = "Reemplazar texto en multiples archivos."
+++
Para reemplazar texto en mltiples archivos en diferentes directorios podemos usar los siguientes comandos de linux.

> find . -name "\*" -exec sed -i "s/reemplazaesto/porestootro/g" {} ;
