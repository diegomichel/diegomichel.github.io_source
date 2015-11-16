+++
date = "2010-03-30"
title = "Como instalar Windows XP en QEMU"
+++
Instalar Qemu:

> aptitude install qemuCrear el disco duro virtual> qemu-img create -f qcow windows.img 6GInstalar desde el cdrom> qemu -localtime -cdrom /dev/cdrom -m 512 -boot d windows.imgO Instalar desde una imagen ISO> qemu -localtime -cdrom cdimagefile.iso -m 512 -boot d windows.img512 es el numero de megabytes de memoria, lo puedes cambiar a mas o menos dependiendo de tu maquina. Una vez instalado podemos ejecutar la maquina virtual con el siguiente comando:> qemu -m 512 -localtime windows.img
