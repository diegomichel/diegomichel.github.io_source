+++
date = "2007-12-29"
title = "Y sigue el Spam..."
+++
Esta vez a sido el [blog de frases](http://blogdefrases.paganar.com) lo mismo que a [versos de amor](http://versosdeamor.info) le "inyectaron" una lista de enlaces al final de la pagina(footer), esto tenia WordPress 2 punto y algo, ya lo he actualizado a la ultima versin, lo extrao es que ahora los enlaces apuntaban a [isopixel.net](http://isopixel.net), ya les he dejado algunos comentarios para que chequn que pasa... otra cosa es que en su blog principal tienen tambin los enlaces ocultos que van a unas paginas dentro de su mismo dominio...

 

Aun no doy con la respuesta sobre como corregirlo lo nico que se es que le ha pasado a dos de mis blogs, ya los he actualizado a la ultima versin de WordPress, pero en isopixel tambin tienen la ultima versin de WordPress y les hackearon aun as... entonces lo que puede ser es el plugin phpexec, que es(era) el nico activo en los dos blogs que me spamearon...si es as entonces ya estara solucionado(espero @.@).

 

&nbsp;

 

Bueno siguiendo... lo que haces estos Spammers, es crear paginas HTML secretas en paginas de otras personas(isopixel), entonces hacen que pase googlebot por la pagina... luego ya que google ha indexado la pagina, hacen un redireccion 301 a la pagina donde en realidad venden las drogas que tratan de promocionar.

 

Por ejemplo si tratas de entrar a esta pagina isopixel.net/?newsid=3 no veras nada, pero si cambias el user agent a Googlebot, voilaaaaa una pagina con texto, con enlaces salientes a cnn y google... por ahora... entonces busque ese mismo texto en google, encontr una pagina y viola!!! redireccion 301 a la pagina de drogas ejemplo isopixel.net/?newsid=83.

 

&nbsp;

 

y ahi esta todo desenvuelto, bueno ojala y alguien sepa la solucin, a muchos les ha pasado pero siempre diferente, a unos les modifican el theme, en mi caso fueron algunos archivos del directorio wp-include :S, a otros la base de datos, as que supongo que usaran distintos bugs...


