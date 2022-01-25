import cv2
import numpy as np
import imutils
import easyocr

from ConverterNew import ConverterNew


def imshow(img):
    cv2.imshow("TEST", img)
    cv2.waitKey(0)


img = cv2.imread(r'examples\4.jpg')
converter = ConverterNew()
converted_img = converter.convert_photo(img)

imshow(converted_img)