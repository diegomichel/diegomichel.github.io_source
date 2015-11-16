+++
date = "2007-11-18"
title = "Me 'hackearon' un blog."
+++
&nbsp;

Pues eso que me han hackeado el blog de [versos de amor](http://versosdeamor.info) (aprovecho el link para que google mire que ya la arregle xD), lo que han hecho es aprovecharse de una vulnerabilidad en el archivo links.php(encargado de agregar los links a la base de datos.) que permite a usuarios registrados agregar links sin permiso.

Pues revisando hoy el posicionamiento en Google me di cuenta que esa pagina bajo en los resultados, y decidí estudiar el problema y cual fue mi sorpresa al ver la caché de Google mostraba tres links los cuales apuntan a un blog de la universidad de Yale:

hxxp://xenon.physics.yale.edu/~nikx/home/wp-content/includes/cache/cialis/buy-cialis.html

hxxp://xenon.physics.yale.edu/~nikx/home/wp-content/includes/cache/cialis/buy-cialis-online.html

hxxp://xenon.physics.yale.edu/~nikx/home/wp-content/includes/cache/cialis/cheap-cialis.html

Los cuales al mismo tiempo redireccionan a:

hxxp://trustedtablets.com/cialis.htm?wm=4497&tr=8027

&nbsp; \*\*\*\*Sustituir las x en hxxp por t\*\*\*\*

En la cual parece que venden viagra o algo así.

Investigue un poco mas del bug y se que afecta a la versión de WordPress 2.3 y todas las anteriores, ese blog tiene una versión anterior a la 2.3 y tenia el registro de usuarios activado, hasta el día de hoy.

También se que existe una solución, la cual es actualizar el archivo links.php, pero parece que solo es para el WordPress 2.3.

En esa pagina tengo demasiados usuarios registrados y no se cual de ellos fue el que hizo semejante atrocidad, así que tendré que borrarlos todos, por ahora no me interesa actualizar WordPress.

En SigT.net nos enseñan [como solucionarlo](http://sigt.net/archivo/exploit-en-wordpress-permite-anadir-enlaces-al-blogroll.xhtml) y ponen un poco mas de información.

WordPress Blogroll Hack


