+++
date = "2010-11-08"
title = "Clase para acceder Mysql desde PHP5"
+++
Como ya existe mysqli(Mysql Improved) en php5 que es orientado a objetos lo unico que tenemos que hacer es extender la clase para convertirla en Singleton, para asi asegurarnos que solo exista una sola conneccion al servidor Mysql en todo momento. Database.php [php]<?php class Database extends mysqli { private static $databaseConnection = NULL; public static function getInstance() { if (!self::$databaseConnection) { self::createInstance(); } return self::$databaseConnection; } function \_\_construct() { @parent::\_\_construct('localhost', 'root', '1', 'blog'); if (mysqli\_connect\_errno()) { throw new Exception( mysqli\_connect\_error(), mysqli\_connect\_errno() ); } } private static function createInstance() { $class = \_\_CLASS\_\_; self::$databaseConnection = new $class; } } ?>[/php] Recuerda que tienes que reemplazar los valores USUARIO\_MYSQL, PASSWORD\_MYSQL y NOMBRE\_DE\_LA\_BASE\_DE\_DATOS por los de tu servidor web. Luego para usarla solo tienes que incluir el archivo Database.php donde quieras. por Ejemplo:. [php] <?php include "Database.php"; $db = Database::getInstance(); $result = $db->query("select \* from users"); $allUsers = $result->fetch\_all(); $result->close(); ... ?> [/php]**$db = Database::getInstance();** Nos devuelve la coneccion a la base de datos y si no existe la crea.**$result = $db->query("select \* from users");** Ejecuta una consulta SQL y guarda el objeto [Mysqli\_Result](http://mx.php.net/manual/en/class.mysqli-result.php) en $result**$allUsers = $result->fetch\_all();** fetch\_all() devuelve un array con todos los resultados de la consulta SQL.**$result->close();** Libera la memoria usada por el objeto $result, se debe ejecutar siempre que el objeto result no sera usado. Puedes checar la referencia de funciones de [mysqli](http://mx.php.net/manual/en/class.mysqli.php) para mas funciones muy utiles como [fetch\_object](http://mx.php.net/manual/en/mysqli-result.fetch-object.php). Rapido y simple.

