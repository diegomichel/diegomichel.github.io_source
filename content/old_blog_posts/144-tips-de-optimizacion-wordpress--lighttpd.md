+++
date = "2010-04-16"
title = "Tips de optimizacion wordpress + lighttpd."
+++
Lo primero que se debe hacer es activar la opcin de cache de lighttpd. abre tu archivo /etc/lighttpd/lighttpd.conf y descomenta el mod\_compress. En mi caso quedo asi.

> server.modules = ( "mod\_access", "mod\_alias", # "mod\_accesslog", "mod\_expire", "mod\_compress", "mod\_fastcgi", "mod\_cgi", "mod\_rewrite", "mod\_setenv", # "mod\_redirect", # "mod\_evhost", # "mod\_usertrack", # "mod\_rrdtool", # "mod\_webdav", # "mod\_expire", # "mod\_flv\_streaming", # "mod\_evasive" )Tambin anade las siguientes lineas:> compress.cache-dir = "/var/cache/lighttpd/compress/" compress.filetype = ("text/plain", "text/html", "application/x-javascript", "text/css", "text/javascript") **compress.cache-dir** es donde se guardan los archivos y **compress.filetype** le dice a lighttpd que archivos se pueden guardar en la cache. Ya con eso tienes la mayoria de los archivos en cache. El caso de php es especial ya que es dinmico, para activar la cache de php, debes editar el archivo php.ini en /etc/php5/cgi/php.ini y descomentar las siguientes lineas:> zlib.output\_compression = On zlib.output\_handler = 1y por ultimo reinicias lighttpd.> /etc/init.d/lighttpd restartNota: Instrucciones basadas en Debian Lenny
