+++
date = "2013-01-28"
title = "How to make Tiled maps load on libgdx."
+++
1.- Download libgdx libs, and put them in for example c:gdxnew 2.- Create your map with tiled and put in a directory example c:mymap 3.- Create an output directory example: c:libgdxmap 4.- open cmd(command line) and execute &nbsp;

> java -cp C:gdxnewgdx.jar;C:gdxnewextensionsgdx-toolsgdx-tools.jar;C:gdxnewextensionsgdx-tiled-preprocessorgdx-tiled-preprocessor.jar com.badlogic.gdx.tiledmappacker.TiledMapPacker c:mymap c:libgdxmapNow you can use the files on c:libgdxmap on your libgdx project :) &nbsp; I was using just the texture packer to generate the the atlas for the map, but you actually need to use the **TiledMapPacker** to make it work, or it will not render/draw your tiled map on **libgdx**.
