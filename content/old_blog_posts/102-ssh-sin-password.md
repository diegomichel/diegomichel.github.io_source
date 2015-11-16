+++
date = "2008-12-29"
title = "SSH sin password"
+++
En la maquina cliente: donde remote es la ip o hostname de la maquina remota. [Al preguntarte por la phrase dejar en blanco y dar enter.]

> local$ ssh-keygen -t dsa local$ scp ~/.ssh/id\_dsa.pub remote: local$ ssh username@remoteEn el servidor> remote$ cat ~/id\_dsa.pub >> ~/.ssh/authorized\_keys remote$ chmod 644 ~/.ssh/authorized\_keys remote$ exitLa proxima vez que uses ssh no te preguntara por el password.
