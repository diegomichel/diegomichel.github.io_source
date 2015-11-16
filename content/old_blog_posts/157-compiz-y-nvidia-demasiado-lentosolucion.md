+++
date = "2011-01-06"
title = "Compiz y Nvidia demasiado lento[Solucion]"
+++
Pues me puse a checar otra vez compiz, lo unico que me alejaba de usarlo era cuando jugaba juegos, y pues como no he jugado ultimamente estoy tratando de usar compiz de nuevo. Ahora si la solucion para el problema de lentitud es la siguiente solamente anade el parametro [raw]"--indirect-rendering"[/raw], en mi caso la linea que uso para correr compiz quedaria de la forma siguiente:

> [RAW]compiz --replace ccp --indirect-rendering[/RAW]
