+++
date = "2010-05-06"
title = "Como montar una particion ext3 en freebsd."
+++
Lo primero que tenemos que hacer es identificar nuestros discos duros.

> localhost# dmesg|grep -i "SATA" atapci0: <ati ixp700 sata300 controller> port 0xff00-0xff07,0xfe00-0xfe03,0xfd00-0xfd07,0xfc00-0xfc03,0xfb00-0xfb0f mem 0xfe02f000-0xfe02f3ff irq 22 at device 17.0 on pci0
> ad4: 715404MB <seagate st3750330as sd04> at ata2-master SATA150
> ad6: 381554MB <seagate st3400832as> at ata3-master SATA150</seagate></seagate></ati>Una vez tenemos localizado el disco en mi caso es el ad4 donde tengo las particiones de linux, ahora tenemos que saber como las nombra freebsd, para ello ejectua:> localhost# ls /dev/ad4\* /dev/ad4 /dev/ad4s2 /dev/ad4s4 /dev/ad4s1 /dev/ad4s3 /dev/ad4s5en este caso los equivalentes para linux serian.> /dev/ad4 -> /dev/sda /dev/ad4s1 -> /dev/sda1 ... etc.Y para pontar la particion ad4s1 es:> mount -t ext2fs /dev/ad4s1 /mnt/s1El directorio /mnt/s1 debe ser creado primero.
