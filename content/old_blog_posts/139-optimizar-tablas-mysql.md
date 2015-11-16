+++
date = "2010-04-06"
title = "Optimizar tablas mysql."
+++
Bueno con el post anterior acerca de [optimizar mysql](http://diegomichel.org/2010/04/04/optimizar-mysql/) con [Mysql Tuner](http://diegomichel.org/2010/04/04/optimizar-mysql/), me encontr con el problema de que tengo muchas bases de datos con muchas tablas asi que me tuve que crear un script para realizar la tarea.

> DBS="$(mysql -pMYSQLPASSWORD -Bse 'show databases')" for db in $DBS do echo $db TABLES="$(mysql -pMYSQLPASSWORD --database=$db -Bse 'show tables')" for table in $TABLES do echo "Optimizing Table $table" mysql -pMYSQLPASSWORD --database=$db -Bse "OPTIMIZE TABLE $table" done doneBasicamente el script lo que hace es tomar la lista de base de datos, luego con esa lista ir pasando en cada una y obtener las tablas, y ya con eso puedes ejecutar OPTIMIZE TABLE. Si deseas utilizar este script cambia MYSQLPASSWORD por tu password de mysql, y copia el contenido en un archivo ponle un nombre por ejemplo optimiza.sh, y para ejecutarlo utiliza la siguiente linea:> sh optimiza.sh
