+++
date = "2013-01-30"
title = "Convertir between screen to world and coordinates libgdx"
+++
> Vector3 mouseCoordinates = new Vector3(screenX,screenY,0); Teeport.camera.unproject(mouseCoordinates); Vector2 playerPosition = Teeport.player.body.getPosition(); Utils.vectorInWorldCoordinates(playerPosition);Just in case i need it again later. &nbsp; Mouse(camera) to world coordinates
1. Unproject mouse coordinates
2. Convert your object position from box2d to world coordinates and thats it :)

