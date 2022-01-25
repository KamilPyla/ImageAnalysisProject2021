import numpy as np
import pytesseract
import cv2

def imshow(img):
    cv2.imshow("Title", img)

pytesseract.pytesseract.tesseract_cmd = r"D:\Dev Tools\Tesseract-OCR\tesseract.exe"

img = cv2.imread(r"example-img\test6.jpg")
img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

img = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
img = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

imshow(img)
text = pytesseract.image_to_string(img)
print(text)

cv2.waitKey(0)