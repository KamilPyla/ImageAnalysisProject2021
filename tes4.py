import cv2
import numpy as np
import imutils
#import pytesseract
import easyocr


def imshow(img):
    cv2.imshow("TEST", img)
    cv2.waitKey(0)

img = cv2.imread(r'examples\2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imshow(gray)

bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
edged = cv2.Canny(bfilter, 30, 200) #Edge detection
imshow(edged)

keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break

#print(location)


mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0,255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)
imshow(mask)

(x,y) = np.where(mask==255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropped_image = gray[x1:x2+1, y1:y2+1]

#gray_cropped = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(cropped_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
thresh = cv2.GaussianBlur(thresh, (3,3), 0)
inverse = ~thresh
imshow(cropped_image)

#pytesseract.pytesseract.tesseract_cmd = r"D:\Dev Tools\Tesseract-OCR\tesseract.exe"
#result = pytesseract.image_to_string(cropped_image)
reader = easyocr.Reader(['en'])
result = reader.readtext(inverse)
text = result[0][-2]

res = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),3)
print(text)
imshow(res)
