import sys
import cv2
import numpy as np

filename = sys.argv[1]

img = cv2.imread(filename, 0)

rows,cols = img.shape

RotMat = cv2.getRotationMatrix2D((cols/2, rows/2), 180, 1)
dst = cv2.warpAffine(img, RotMat, (rows, cols))

cv2.imshow('image', dst)
cv2.imwrite('ans2.png', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
