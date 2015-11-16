+++
date = "2009-07-08"
title = "Teclado multimedia nombre de las teclas."
+++
Bueno acabo de cambiar mi Window Manager a ion3, y quiero utlizar las teclas de mi teclado para controlar el reproductor de musica, en este caso mocp. El comando para hacer debug a los eventos del teclado es:

> xevlo ejecutas, presiona la tecla la cual necesitas hacer bind y te apareceran algunos datos:> KeyPress event, serial 33, synthetic NO, window 0x2400001, root 0x13c, subw 0x0, time 338343028, (85,-9), root:(1180,229), state 0x10, keycode 171 (keysym 0x1008ff17, XF86AudioNext), same\_screen YES, XLookupString gives 0 bytes: XmbLookupString gives 0 bytes: XFilterEvent returns: FalseLa parte que nos interesa es:> keycode 171 (keysym 0x1008ff17, XF86AudioNext)en mi caso yo uso ion asi que agregado la linea:> kpress("XF86AudioNext", "ioncore.exec\_on(\_, 'mocp --next')"),en el archivo cfg\_ioncore.lua, en la seccion adecuada y reinicion ion3, y listo. Keywords: ion3, linux, teclado, teclado multimedia, bind keys, keyboard binds, binding keys, bind keys, bind teclado, crear binds.
