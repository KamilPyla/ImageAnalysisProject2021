from Worker import Worker
import cv2
import numpy as np

img = r'examples\2.jpg'

w = Worker(img)

def imshow(img):
    cv2.imshow("TEST", img)
    cv2.waitKey(0)


imshow(cv2.imread(img))

w.do_your_work()

imshow(w.image_with_frame)

print(w.numbers)
