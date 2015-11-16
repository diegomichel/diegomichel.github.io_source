+++
date = "2013-01-08"
title = "Dibujar linea en libgdx"
+++
` ShapeRenderer shapeRenderer = new ShapeRenderer();
                  shapeRenderer.begin(ShapeType.Line);
                  shapeRenderer.setColor(1, 1, 0, 1);
                  shapeRenderer.line(x1, y1, x2, y2);
                  shapeRenderer.end();`
