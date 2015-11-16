+++
date = "2010-04-17"
title = "Montar Ext4 en Debian Lenny."
+++
Debian Lenny no soporta el formato Ext4 oficialmente, por que era experimental en el momento en que Lenny fue lanzada, pero tenia un driver experimental que puedes usar para leer los archivos.

> tune2fs -E test\_fs /dev/sdax mount -t ext4dev -o ro /dev/sdax /mnt/sdax
