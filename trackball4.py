# -*- coding: cp1252 -*-
import SimpleCV
from SimpleCV import Image
 
display = SimpleCV.Display()

img = Image("ping/source/image4.jpeg")

# parametre pour image1 : (stretch(200,255), isCircle(0.2)
# parametre pour image2 : non trouvé
# parametre pour image3 : (stretch(2,120), isCircle(0.2)
# parametre pour image4 : (stretch(2,120), isCircle(0.2)
# parametre pour image5 : (stretch(2,120), isCircle(0.2)
# parametre pour image6 : plante
# parametre pour image7 : non trouvé
            
dist = img.colorDistance(SimpleCV.Color.ORANGE).dilate(2)

segmented = dist.stretch(2,120).invert()

blobs = segmented.findBlobs()

if blobs:

        balles = blobs.filter([b.isCircle(0.2) for b in blobs])
                
        if balles:
                for balle in balles:
                        img.drawCircle((balle.x,balle.y),balle.radius(),SimpleCV.Color.BLUE,3 )

img.show()


