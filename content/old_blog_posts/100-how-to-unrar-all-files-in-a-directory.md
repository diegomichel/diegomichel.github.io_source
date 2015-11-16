+++
date = "2008-12-28"
title = "How to unrar all files in a directory"
+++
En espaol como descomprimir todos los rar de un directorio:`find . -name '*.rar' -exec unrar x {} ;`usar esta en caso de que sean archivos de varias partes.`find . -name '*part1.rar' -exec unrar x {} ;`Si lo quieren convertir en un comando simplemente gurdenlo en un archivo, por ejemplo unrarall, luego chmod +x unrarall, y lo mueve a /usr/bin/ con sudo mv unrarall /usr/bin/ y listo nomas necesitaran escribir unrarall la prxima vez. unrar all files bash script, script unrar all files, descomprimir todos los archivos rar en un directorio, script bash para descomprimir todos los archivos rar de un directorio.


