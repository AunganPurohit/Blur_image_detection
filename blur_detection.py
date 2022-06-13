from imutils import paths 
import cv2 as cv
import numpy as np
#mport pandas as pd

imagepaths = list(paths.list_images("C:\images"))

for imagePath in imagepaths:
 images = cv.imread(imagePath,cv.IMREAD_GRAYSCALE)
 lap_var = cv.Laplacian(imagePath, cv.CV_64F).var()
 #print(lap_var)

 not_blurry = 0
 blurry = 0
 if lap_var<5:
    blurry = blurry + 1
 else:
    not_blurry = not_blurry +1

print(blurry)
print(not_blurry)
    

#cv.imshow("Img",img)
cv.destroyAllWindows()

