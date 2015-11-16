+++
date = "2010-04-15"
title = "Reinstalar archivos de configuracion de debian."
+++
Me he encontrado con este problema de que si instalas un paquete lo remueves y lo reinstalas otra vez, algunas veces omite instalar el archivo de configuracin. Solucin:

> apt-get --purge remove Paquete aptitude install Paquetey queda como nuevo.
