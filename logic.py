import cv2 as cv
import matplotlib.pyplot as plt
import reader

r = reader.ReaderGrey('images/car_3.png')
# img = r.image

img = r.image
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)

cv.imshow('image',thresh2)
cv.waitKey(0)
cv.destroyAllWindows()