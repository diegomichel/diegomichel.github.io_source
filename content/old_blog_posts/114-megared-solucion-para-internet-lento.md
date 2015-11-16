+++
date = "2009-12-25"
title = "Megared Solucion para internet lento."
+++
Si tienes megared, linux y piensas que el internet te va mas lento de lo normal(en comparacion con windows p. ej.), puede que tengas razon. Al parecer los routes de megared estan "broken" aka danados o mal configurados[http://lwn.net/Articles/92727/]. Para el dia de hoy ha cambiado un poco la configuracion del kernel de linux asi que el fix que recomiendad en ese articulo se traduce a ejecutar las siguientes lineas.

> sudo touch /proc/sys/net/ipv4/tcp\_window\_scaling sudo echo 0 > /proc/sys/net/ipv4/tcp\_window\_scalingprueba si tu velocidad de descarga mejoro, si es asi para que los cambios sean permanentes agrega esto al archivo /etc/sysctl.conf.> net.ipv4.tcp\_window\_scaling = 0
